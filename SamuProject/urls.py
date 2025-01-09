from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/medicines/', include('medicines.urls')),
    path('api/v1/administrators', include('administrators.urls')),
    path('api/v1/patients', include('patients.urls')),
    path('api/v1/patientcares', include('patient_cares.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
