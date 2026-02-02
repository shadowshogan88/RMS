from django.db import models
from django.contrib.auth.models import AbstractUser


class CategoryModels(models.Model):
    name = models.CharField(max_length=50, blank=True, unique=True)
    description = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.name}'


class ContactMessage(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_WORKING = 'working'
    STATUS_COMPLETE = 'complete'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_WORKING, 'Working'),
        (STATUS_COMPLETE, 'Complete'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

class AuthUserModel(AbstractUser):
    ROLES = [
        
        ('Admin','Admin'),
        
        ('User','User'),
        ]

    user_role = models.CharField(max_length=20,choices=ROLES,null=True)
    
    def __str__(self):
        return f'{self.username}-{self.user_role}'


class Recipe(models.Model):
    STATUS_WORKING = 'working'
    STATUS_PUBLISHED = 'published'

    STATUS_CHOICES = [
        (STATUS_WORKING, 'Working'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    title = models.CharField(max_length=150)
    preparation_time = models.CharField(max_length=50)
    cooking_time = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=30)
    serves = models.CharField(max_length=30)
    category = models.ForeignKey(CategoryModels, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    photo = models.ImageField(upload_to='recipes/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_WORKING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
