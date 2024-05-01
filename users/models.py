from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    ROLES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=30, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='фамилия', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='номер телефона', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=5, choices=ROLES, default='user')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
