from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer,UserRegistrationSerializer
from .models import Post
from users.models import CustomUser
# Create your views here.

class Postlist(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateUserView(generics.CreateAPIView):
    queryset =CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer