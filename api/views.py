from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from posts.models import Post
from posts.serializers import PostSerializer
from categorys.models import Category
from categorys.serializers import CategorySerializer,CategorySearchSerializer
from salons.models import Salon
from salons.serializers import SalonSerializer


@api_view(["GET"])
def home(request):
    posts = PostSerializer(Post.objects.all(), many=True).data
    if len(posts) == 0:
        posts = None

    categorys = CategorySerializer(Category.objects.filter(pk__in=[1, 2, 3]), many=True).data
    if len(categorys) == 0:
        categorys = None

    salons = SalonSerializer(Salon.objects.all().filter(isSpecial=True), many=True).data
    if len(salons) == 0:
        salons = None

    return Response(
        {
            "posts": posts,
            "categorys": categorys,
            "specialOffersSalon": salons
        }
    )


@api_view(["GET"])
def search(requests):
    s = requests.query_params.get('s', None)
    categoryS = requests.query_params.get('category', None)
    salons = ""
    if categoryS is not '':
        categoryS = categoryS.split(",")
        salons = Salon.objects.filter(Q(category__name__in=categoryS))
    else:
        salons = Salon.objects.all()
    if s is not '':
        salons = salons.filter(Q(name__icontains=s) | Q(description__icontains=s))
        return Response(SalonSerializer(salons, many=True).data)
    else:
        salons = salons.all()
        return Response(SalonSerializer(salons, many=True).data)


@api_view(["GET"])
def allCategoryNameForSearch(requests):
    categoryNames = Category.objects.all()
    return Response(CategorySearchSerializer(categoryNames,many=True).data)

