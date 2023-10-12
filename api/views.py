from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

# Create your views here.

def test(request):
    return HttpResponse("test")

@api_view(["GET"])
def allPost(request):
    posts = Post.objects.all()
    selposts = PostSerializer(posts,many=True)
    return Response(selposts.data)

@api_view(["GET"])
def getPost(request, id):
    post = Post.objects.get(id=id)
    selpost = PostSerializer(post,many=False)
    return Response(selpost.data)


