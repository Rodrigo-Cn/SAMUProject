from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorView.as_view()),
    path('<int:id>/', views.DoctorViewDetail.as_view())
]
