from rest_framework import viewsets

from .serializers import CoffeeSerializer, PostSerializer
from .models import Coffee, Post


class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all().order_by('name')
    serializer_class = CoffeeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

# from django.shortcuts import render
# from django.http import HttpResponse
# test


# # def coffee(request):
# #     return HttpResponse("Hello world!")

# # from django.http import HttpResponse
# # from django.template import loader


# # def coffee(request):
# #     template = loader.get_template('sample.html')
# #     return HttpResponse(template.render())
