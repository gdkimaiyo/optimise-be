from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('unoptimized', views.unoptimized_posts, name='unoptimized_posts'),
    # path('optimized', views.optimized_posts, name='optimized_posts'),
]
