from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManger
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = [('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')]

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    objects = UserManger()
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return f'{self.nombres} {self.apellidos}'
    
     
    