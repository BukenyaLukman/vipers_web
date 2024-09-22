from django.conf import settings
from rest_framework import generics, permissions, status, views, exceptions
from .serializers import (
    RegisterSerializer, 
    LoginSerializer, 
    ResetPasswordEmailRequestSerializer, 
    SetNewPasswordSerializer, 
    LogoutSerializer,
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt

