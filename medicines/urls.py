from django.urls import path
from . import views

urlpatterns = [
    path('', views.MedicineAPI.as_view()),
    path('<int:id>', views.MedicineAPIDetail.as_view())
]
