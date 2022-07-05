from django.urls import path,include
from .views import PostView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('posts', PostView)

app_name = 'posts'

urlpatterns = [
    path('', include(router.urls))
]