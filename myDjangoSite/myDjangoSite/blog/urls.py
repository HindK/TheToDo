from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	#path('', views.home, name='blog-home'),
	path('posts/', views.PostListCreate.as_view() ),
	#path('about/', views.about, name='blog-about'),

]
