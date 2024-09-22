from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


ROLES = (
    ('admin', 'admin'),
    ('fans', 'fans'),
    ('player', 'player'),
    ('coach', 'coach'),
    ('manager', 'manager'),
    ('student', 'student'),
    ('teacher', 'teacher'),
    ('super_fans', 'super_fans'),
    ('merchants', 'merchants'),
)


class UserManager(BaseUserManager):

    def create_user(self,username,phone, email, password=None,  **extra_fields):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have an email')

        user = self.model(
            username=username, 
            email=self.normalize_email(email),
            phone=phone, 
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(
            username, email, password, **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        FANS = 'fans'
        PLAYER = 'player'
        COACH = 'coach'
        MANAGER = 'manager'
        STUDENT = 'student'
        TEACHER = 'teacher'
        SUPER_FANS = 'super_fans'
        MERCHANTS = 'merchants'

    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone = models.CharField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.FANS)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']


    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.username


    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }