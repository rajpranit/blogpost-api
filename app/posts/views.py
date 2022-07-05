from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts
from . import serializers

class PostView(viewsets.ModelViewSet):

    serializer_class = serializers.Posts
    queryset = Posts.objects.all()

    def get_serializer_class(self):
        return self.queryset.order_by(-1)

