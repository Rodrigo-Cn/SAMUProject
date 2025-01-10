from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientView.as_view()),
    path('<int:id>/', views.PatientViewDetail.as_view())
]
