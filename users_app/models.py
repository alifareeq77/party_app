from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, password,username, email, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):

        return self.create_user(email,username, password, is_staff=True,is_active=True,is_superuser=True, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=256)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=145, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ('name', 'email')

    def __str__(self):
        return self.name
