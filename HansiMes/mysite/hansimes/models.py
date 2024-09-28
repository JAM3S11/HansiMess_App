from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.
class ContactMess(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Message = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.Name}'


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Specify additional fields if needed

    def __str__(self):
        return self.username
