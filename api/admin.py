from django.contrib import admin
from .models import Category, Project, Contact, UserProfile, Blog, ProjectImage
# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Blog)