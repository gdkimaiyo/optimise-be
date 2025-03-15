from django.shortcuts import render

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to Optimization Demo"})