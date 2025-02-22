from django.urls import path , include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('hello/', views.hello),
    path('', include(router.urls)),
  
]