from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from .views import LogoutView, getChartParameters
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/medicines/', include('medicines.urls')),
    path('api/v1/administrators/', include('administrators.urls')),
    path('api/v1/patients/', include('patients.urls')),
    path('api/v1/patientcares/', include('patientcares.urls')),
    path('api/v1/chartparameters/', getChartParameters),
    path('api/v1/authentication/login/', views.obtain_auth_token),
    path('api/v1/authentication/logout/', LogoutView.as_view()),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/documentation/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/documentation/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/documentation/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
