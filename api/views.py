from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from persons.serializers import PersonSerializer
from posts.models import Post
from posts.serializers import PostSerializer
from categorys.models import Category
from categorys.serializers import CategorySerializer
from salons.models import Salon
from salons.serializers import SalonSerializer
from persons.models import Person



@api_view(["GET"])
def home(request):
    posts = PostSerializer(Post.objects.all(), many=True).data
    if len(posts) is 0:
        posts = None

    categorys = CategorySerializer(Category.objects.filter(pk__in=[1, 2, 3]), many=True).data
    if len(categorys) is 0:
        categorys = None

    salons = SalonSerializer(Salon.objects.all().filter(isSpecial=True), many=True).data
    if len(salons) is 0:
        salons = None

    return Response(
        {
            "posts": posts,
            "categorys": categorys,
            "specialOffersSalon": salons
        }
    )


@api_view(['POST'])
def regester(request):
    user = Person.objects.get(username = request.POST["username"])
    if user is not None:
        return Response({"statos": "is exits"})

    users = PersonSerializer(data=request.POST)
    if users.is_valid():
        users.save()
        return Response({"statos": "ok"})

    else:
        return Response({"statos": "erorr"})

