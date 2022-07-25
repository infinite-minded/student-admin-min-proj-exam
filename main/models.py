import pathlib
import uuid
from calendar import month
from enum import auto
from operator import mod
from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime
from django.utils.timezone import now

def default_start_time():
    now = datetime.now()
    start = now.replace(microsecond=0)
    ans = start.strftime("%I:%M %p %d/%m/%Y")
    return ans

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return "%d" % (self.id)

class Student(models.Model):
    unique_id = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    clas = models.CharField(max_length=6)
    rollno = models.IntegerField(default=0)
    g1 = models.IntegerField(default=0)
    g2 = models.IntegerField(default=0)
    g3 = models.IntegerField(default=0)
    total = models.IntegerField(default=0,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Ranklist(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)