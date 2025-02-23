from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
def hello(request):
    return JsonResponse({'message': 'Hello, World!'})

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
    
    filter_backends =[DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title' , 'content']
    ordering_fields = ['title' , 'created_at']


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    