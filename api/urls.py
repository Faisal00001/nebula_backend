from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(), name='Home_page'),
    path('projects/',views.ProjectListView.as_view(), name='all_projects'),
    path('projects/<int:id>/', views.ProjectDetailView.as_view(), name='specific_project'),
    path('contact/', views.submission_query, name='user_query_submission'),
    path('profiles/', views.UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<str:username>/', views.UserDetailView.as_view(), name='userprofile-details'),
    path('blogs/', views.BlogListView.as_view(), name='all_blogs'), 
    path('blogs/<int:id>/', views.BlogDetailView.as_view(), name='blog-details'),
]