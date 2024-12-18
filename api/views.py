from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Project, Category, UserProfile, Blog
from .serializers import ProjectSerializer, BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactSerializer, UserProfileSerializer
from django.utils import timezone
from datetime import timedelta


# Create your views here.

class HomePageView(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        profiles_serializer = UserProfileSerializer(profiles, many=True)

        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)

        recent_timeframe = timezone.now() - timedelta(days=60)
        recent_blogs = Blog.objects.filter(date_posted__gte=recent_timeframe)

        blogs_serializer = BlogSerializer(recent_blogs, many=True)

        data = {
            'profiles': profiles_serializer.data,
            'projects': projects_serializer.data,
            'recent_blogs': blogs_serializer.data,
        }

        return Response(data)

class UserProfileList(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetailView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'

    def get_object(self):
        username = self.kwargs['username']
        return self.queryset.get(user__username=username)


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'


class ProjectListView(ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        category_parameter = self.request.query_params.get('category', None)  
        if category_parameter:
            return Project.objects.filter(category__name__icontains=category_parameter) 
        return Project.objects.all() 
    

class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'
    

@api_view(['POST'])
def submission_query(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        send_mail(
            subject="New User Query Submitted!",
            message=f"A new query has been submitted by {serializer.validated_data['first_name']} {serializer.validated_data['last_name']} {serializer.validated_data['email']} for {serializer.validated_data['service']}.\n\nMessage: {serializer.validated_data['message']}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_NOTIFICATION_EMAIL],
            fail_silently=False,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)