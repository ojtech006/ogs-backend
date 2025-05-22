from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('contact', ContactMessageViewSet, basename='contact-message')
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
