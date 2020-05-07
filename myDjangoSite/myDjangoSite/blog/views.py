from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post 
from .serializers import PostSerializer
from rest_framework import generics

'''posts = [ 
	{
		'author': 'ShreyaPuranik',
		'title': 'Intro to Django',
		'content': 'Learning the basics of Django now',
		'date': '7th May 2020',
	},
	{
		'author': 'HKG',
		'title': 'Intro to React',
		'content': 'Learning the basics of React now',
		'date': '7th May 2020',
	}

]'''

class PostListCreate( generics.ListCreateAPIView ):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

'''class PostList( APIView ):

	def get( self, request ):
		posts = Post.objects.all()
		serializer = PostSerializer( posts, many=True )
		return Response(serializer.data)

	def post( self, postData ):
		serializer = PostSerializer( data=postData )
		serializer.isValid(raise_exception=True)
		serializer.save()'''
		#pass



# Create your views here.

'''def home(request):
	context = {
		'posts' : posts,
	}
	return render(request, 'blog/home.html', context) #Still returns an HTTPResponse

def about(request):
	context = {
		'title' : 'Learning about Django',
	}
	return render( request, 'blog/about.html', context )'''