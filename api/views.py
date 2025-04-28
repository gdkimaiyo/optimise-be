import requests
import time

# rest_framework
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

from api.models import User
from .serializers import PostSerializer, UserSerializer

from api.doc import (get_posts_data_doc)


# Create your views here.
# @api_view(["GET"])
# def home(request):
#     return Response({"message": "Welcome to Optimization Demo"})


@api_view(['GET'])
def unoptimized_posts(request):
    start_time = time.time()
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    serializer = PostSerializer(posts, many=True)
    end_time = time.time()
    total_time_secs = end_time - start_time
    total_time_milli_secs = total_time_secs * 1000

    print(f"Unoptimized: Response time: {total_time_secs:.2f} seconds")
    print(
        f"Unoptimized: Response time: {total_time_milli_secs:.2f} milliseconds")
    return Response(serializer.data)


# @swagger_auto_schema(**get_posts_data_doc)
@api_view(['GET'])
def optimized_posts(request):
    start_time = time.time()
    cached_posts = cache.get('jsonplaceholder_posts')
    if cached_posts is None:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        posts = response.json()
        cache.set('jsonplaceholder_posts', posts, 3600)  # Cache for 1 hour
    else:
        posts = cached_posts

    serializer = PostSerializer(posts, many=True)
    end_time = time.time()
    total_time_secs = end_time - start_time
    total_time_milli_secs = total_time_secs * 1000

    print(f"Optimized: Response time: {total_time_secs:.2f} seconds")
    print(
        f"Optimized: Response time: {total_time_milli_secs:.2f} milliseconds")
    return Response(serializer.data)


@api_view(['GET'])
def users_data(request):
    cached_users = cache.get('dummy_users')
    if cached_users is None:
        users = [
            User(1, "admin", "password123",
                 "admin@example.com", "1234-5678-9012-3456"),
            User(2, "user1", "securepass",
                 "user1@example.com", "9876-5432-1098-7654"),
            User(3, "testuser", "testpass",
                 "test@test.com", "1111-2222-3333-4444"),
        ]

        serializer = UserSerializer(users, many=True)
        cached_users = serializer.data
        cache.set('dummy_users', cached_users, 3600)  # Cache for 1 hour
    else:
        serializer = UserSerializer(cached_users, many=True)

    return Response(serializer.data)
