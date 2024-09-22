from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, 
        min_length=6, 
        write_only=True,
        error_messages={
            "min_length": "Password must be at least {min_length} characters long",
        })
    default_error_messages = {
        'error': 'Something went wrong while creating your account...'
    }

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        phone = attrs.get('phone', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages
            )
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Email already exists'
            )
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Username already exists'
            )
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError(
                'Phone number already exists'
            )
        if not email:
            raise serializers.ValidationError(
                self.default_error_messages
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens','role','phone']

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }
    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens','role','phone']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin', 401)
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified', 401)

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
            'role': user.role,
            'phone': user.phone
        }

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=6)

    class Meta:
        fields = ['email']

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=128, write_only=True)

    class Meta:
        fields = ['password']

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')