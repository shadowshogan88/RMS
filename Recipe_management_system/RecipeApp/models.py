from django.db import models
from django.contrib.auth.models import AbstractUser


class CategoryModels(models.Model):
    name = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.name}'

class AuthUserModel(AbstractUser):
    ROLES = [
        
        ('Admin','Admin'),
        
        ('User','User'),
        ]

    user_role = models.CharField(max_length=20,choices=ROLES,null=True)
    
    def __str__(self):
        return f'{self.username}-{self.user_role}'
