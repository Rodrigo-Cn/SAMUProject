from django.urls import path
from . import views

urlpatterns = [
    path('', views.MedicineAPIView.as_view()),
    path('<int:id>/', views.MedicineAPIViewDetail.as_view())
]
