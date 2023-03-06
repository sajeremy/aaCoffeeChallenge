# from django.conf.urls import url
from django.urls import path, include
from .views import (
    CoffeePingView,
    PostPingView,
    CoffeeListView,
    CoffeeDetailView,
    PostListView,
    PostDetailView

)

urlpatterns = [
    path('api/post/ping', PostPingView.as_view()),
    path('api/coffee/ping', CoffeePingView.as_view()),
    path('api/coffee', CoffeeListView.as_view()),
    path('api/coffee/<int:coffee_id>/', CoffeeDetailView.as_view()),
    path('api/post', PostListView.as_view()),
    path('api/post/<int:post_id>/', PostDetailView.as_view())
]


# # from django.urls import include, path
# # from rest_framework import routers
# # from . import views

# # router = routers.DefaultRouter()
# # router.register(r'coffees', views.CoffeeViewSet)
# # router.register(r'posts', views.PostViewSet)

# # urlpatterns = [
# #     path('', include(router.urls)),
# #     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# # ]


# from . import views

# urlpatterns = [
#     path('coffee/', views.coffee, name='coffee'),
# ]
