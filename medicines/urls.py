from django.urls import path
from . import views

urlpatterns = [
    path('', views.MedicineView.as_view()),
    path('<int:id>/', views.MedicineViewDetail.as_view())
]
