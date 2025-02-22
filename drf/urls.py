from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('hello/', views.hello),
   path('articles/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),

]