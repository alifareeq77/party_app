from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    # Custom manager for UserAccount
    def create_user(self, password, username, email, **kwargs):
        # Create a regular user
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, username, email, **kwargs):
        # Create a superuser with staff and admin privileges
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    # Custom User Account model
    username = models.CharField(unique=True, max_length=256)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=145, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ('name', 'email')

    def __str__(self):
        return self.name
