from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# import uuid
# from django.utils.text import slugify
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True) 
    description = models.TextField(null=True, blank=True)
    linkedin_profile = models.URLField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.user.id} - {self.user.first_name} {self.user.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Project(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.title}'
    
class ProjectImage(models.Model):
    image = models.ImageField(upload_to='img/', null=True, blank=True) 
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project.title} - {self.image.url}'
    

class Blog(models.Model):
    writers = models.ManyToManyField(User, related_name='blogs')  
    date_posted = models.DateTimeField(auto_now_add=True)  
    title = models.CharField(max_length=255)  
    content = models.TextField()  
    image = models.ImageField(upload_to='img/', blank=True, null=True) 
    
    def __str__(self):
        return f'{self.id} - {self.title}'
    

class Contact(models.Model):
    SERVICES = [
        ('Web development', 'Web development'),
        ('Data Analysis', 'Data Analysis'),
        ('Machine Learning', 'Machine Learning'),
        ('Mobile Application', 'Mobile Application'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    service = models.CharField(max_length=50, choices=SERVICES)
    message = models.TextField()
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email} - {self.service}'


