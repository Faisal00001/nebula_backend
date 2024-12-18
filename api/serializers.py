from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Project, Contact, UserProfile, Blog, ProjectImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProjectSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'category', 'images']

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'service', 'message', 'submission_time']
        read_only_fields = ['submission_time']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number', 'address', 'image', 'description', 'linkedin_profile']

class BlogSerializer(serializers.ModelSerializer):
    writers = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'writers', 'date_posted', 'title', 'content', 'image']