from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *

# Create your views here.

def hello(request):
    return JsonResponse({'message': 'Hello, world!'})


class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    def get(self , request , pk):
        article = get_object_or_404(Article , pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self , request , pk):
        article = get_object_or_404(Article , pk=pk)
        serializer = ArticleSerializer(article , data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk):
        article = get_object_or_404(Article , pk=pk)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)