from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .models import Store
from .serializers import PostSerializer
from djlee.models import *
from .serializers import NearStoreSerializer

from django.http import HttpResponse
    
def get_list_near_store(request):
    queryset = Store.objects.all()
    temp='2'
    for row in queryset:
        temp=row.URL
    return HttpResponse("106.10.35.40:8000/media/"+temp)
class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
