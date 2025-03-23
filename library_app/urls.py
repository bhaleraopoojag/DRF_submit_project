
from django.urls import path,include
from .views import BookViewSet,StudentViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'books',BookViewSet)
router.register(r'students',StudentViewSet)

urlpatterns = [
    path('',include(router.urls))
]