from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class PostSerializer( serializers.ModelSerializer ):

	class Meta:
		model = models.Post
		fields = [ 'title', 'content', 'author', 'date']