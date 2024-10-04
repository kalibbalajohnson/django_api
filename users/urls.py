# from django.urls import path
# from . import views

# urlpatterns = [
#     path('/status', views.app_status, name='app_status'),
# ]

# users/urls.py
from django.urls import path
from .views import get, create  

urlpatterns = [
    path('status/', get, name='app_status'), 
    path('status/', create, name='app_post'), 
]
