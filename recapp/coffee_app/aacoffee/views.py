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
        # return HttpResponse('Hello, World!')
        return Response(status=status.HTTP_200_OK)


class CoffeeListView(APIView):
    def get(self, req):
        coffees = Coffee.objects.order_by('name')  # .all()
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
                {"res": f'Object with coffee id: {coffee_id} does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CoffeeSerializer(coffee_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # from rest_framework import viewsets

    # from .serializers import CoffeeSerializer, PostSerializer
    # from .models import Coffee, Post

    # class CoffeeViewSet(viewsets.ModelViewSet):
    #     queryset = Coffee.objects.all().order_by('name')
    #     serializer_class = CoffeeSerializer

    # class PostViewSet(viewsets.ModelViewSet):
    #     queryset = Post.objects.all().order_by('title')
    #     serializer_class = PostSerializer
