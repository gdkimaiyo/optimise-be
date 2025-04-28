from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('optimized', views.optimized_posts, name='optimized_posts'),
    path('unoptimized', views.unoptimized_posts, name='unoptimized_posts'),
    path('users', views.users_data, name='users_data'),
]
