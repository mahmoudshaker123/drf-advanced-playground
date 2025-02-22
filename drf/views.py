from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article

# Create your views here.

def hello(request):
    return JsonResponse({'message': 'Hello, world!'})


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        return Response({'articles': articles.values()})
    