import requests
import time

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .serializers import PostSerializer


# Create your views here.
@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to Optimization Demo"})


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
    print(f"Unoptimized: Response time: {total_time_milli_secs:.2f} milliseconds")
    return Response(serializer.data)


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
    print(f"Optimized: Response time: {total_time_milli_secs:.2f} milliseconds")
    return Response(serializer.data)
