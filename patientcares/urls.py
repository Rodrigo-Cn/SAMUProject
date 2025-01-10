from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientCareView.as_view()),
    path('<int:id>/', views.PatientCareViewDetail.as_view())
]
