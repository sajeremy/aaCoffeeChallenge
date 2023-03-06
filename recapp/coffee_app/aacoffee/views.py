from django.views import View
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .serializers import CoffeeSerializer, PostSerializer
from .models import Coffee, Post


class CoffeePingView(APIView):
    def get(self, req):
        return Response(status=status.HTTP_200_OK)


class PostPingView(APIView):
    def get(self, req):
        return Response(status=status.HTTP_200_OK)


class CoffeeListView(APIView):
    def get(self, req):
        order = req.GET.get("ord")
        if order == "dsc":
            coffees = Coffee.objects.order_by('-name')
        else:
            coffees = Coffee.objects.order_by('name')

        serializer = CoffeeSerializer(coffees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, req):
        coffee_data = {
            'name': req.data.get('name'),
            'year': req.data.get('year'),
            'caffine_content': req.data.get('caffine_content'),
            'caffine_percentage': req.data.get('caffine_percentage')
        }
        serializer = CoffeeSerializer(data=coffee_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoffeeDetailView(APIView):
    def get_object(self, coffee_id):
        try:
            return Coffee.objects.get(id=coffee_id)
        except Coffee.DoesNotExist:
            return None

    def get(self, req, coffee_id):
        coffee_instance = self.get_object(coffee_id)
        if not coffee_instance:
            return Response(
                {"res": f'Object with coffee id:{coffee_id} does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CoffeeSerializer(coffee_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, req, coffee_id):
        coffee_instance = self.get_object(coffee_id)
        if not coffee_instance:
            return Response(
                {"res": f'Object with coffee id:{coffee_id} does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        coffee_instance.delete()
        return Response(
            {"res": "Coffee deleted!"},
            status=status.HTTP_200_OK
        )


class PostListView(APIView):
    def get(self, req):
        # using url query params - ?ord=asc or ?ord=dsc
        order = req.GET.get("ord")
        if order == "dsc":
            posts = Post.objects.order_by('-created_at')
        else:
            posts = Post.objects.order_by('created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, req):
        post_data = {
            'title': req.data.get('title'),
            'coffee': req.data.get('coffee'),
            'text': req.data.get('text'),
            'rating': req.data.get('rating')
        }
        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def get(self, req, post_id):
        post_instance = self.get_object(post_id)
        if not post_instance:
            return Response(
                {"res": f'Object with post id:{post_id} does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostSerializer(post_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, req, post_id):
        post_instance = self.get_object(post_id)
        if not post_instance:
            return Response(
                {"res": f'Object with post id:{post_id} does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        post_instance.delete()
        return Response(
            {"res": "Post deleted!"},
            status=status.HTTP_200_OK
        )
