from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from posts.models import Post
from posts.serializers import PostSerializer
from categorys.models import Category
from categorys.serializers import CategorySerializer
from salons.models import Salon
from salons.serializers import SalonSerializer


@api_view(["GET"])
def home(request):
    posts = PostSerializer(Post.objects.all(), many=True).data
    if len(posts) is 0:
        posts = None

    categorys = CategorySerializer(Category.objects.filter(pk__in=[1, 2, 3]), many=True).data
    if len(categorys) is 0:
        categorys = None

    salons = SalonSerializer(Salon.objects.filter(pk__in=[1, 2, 3]), many=True).data
    if len(salons) is 0:
        salons = None

    return Response(
        {
            "posts": posts,
            "categorys": categorys,
            "salon": salons
        }
    )
