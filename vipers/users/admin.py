from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'phone', 'role', 'is_staff', 'is_superuser', 'is_active')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'phone', 
            'password', 
            'role', 
            'is_staff', 
            'is_superuser', 
            'is_active',
        )

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email', 
        'phone', 
        'role', 
        'is_staff', 
        'is_superuser', 
        'is_verified',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_staff', 'is_superuser', 'is_verified')
    fieldsets = (
        (None, {'fields': (
            'email', 'password'
            )}),
        ('Personal info', {'fields': ('first_name','last_name', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_verified')}),
        ('Roles', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2', 'role', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)