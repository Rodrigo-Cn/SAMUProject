from django.urls import path
from . import views

urlpatterns = [
    path('credentials/', views.getUserInfo, name='user_info'),
    path('permission/', views.getUserPermission, name='user_permission'),
    path('notpermission/', views.getNotPermission, name='user_notpermission'),
]
