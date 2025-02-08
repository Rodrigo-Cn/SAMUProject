from django.urls import path
from .views import getNotPermission, getUserInfo, getUserPermission

urlpatterns = [
    path('credentials/', getUserInfo, name='user_info'),
    path('permission/', getUserPermission, name='user_permission'),
    path('notpermission/', getNotPermission, name='user_notpermission'),
]
