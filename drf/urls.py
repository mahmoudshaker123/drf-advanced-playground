from django.urls import path, include
from . import views
from .views import ArticleViewSet  # استيراد واضح بدلاً من import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# إنشاء الراوتر وتسجيل الـ ViewSet
router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('hello/', views.hello),
    path('api/', include(router.urls)),  # التأكد من تضمين الـ API URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
