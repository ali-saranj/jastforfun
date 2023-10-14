# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Post, User, Salon
# from .serializers import PostSerializer, UserSerializer, SalonSerializer
#
#
# # Create your views here.
# @api_view(["GET", "POST"])
# def allPost(request):
#     try:
#         print(request.data)
#         posts = Post.objects.all()
#         selposts = PostSerializer(posts, many=True)
#         return Response(selposts.data)
#     except:
#         return Response({"e": "e"})
#
#
# @api_view(["GET"])
# def getPost(request, id):
#     post = Post.objects.get(id=id)
#     selpost = PostSerializer(post, many=False)
#     return Response(selpost.data)
#
#
# @api_view(['GET'])
# def getSalon(request):
#     salon = Salon.objects.all()
#     selSalon = SalonSerializer(salon, many=True)
#     return Response(selSalon.data)
