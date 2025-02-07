from django.urls import path
from . import views

urlpatterns = [
    path('credentials/', views.getUserInfo, name='user_info'),
]
