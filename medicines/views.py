from django.shortcuts import HttpResponse
from django.views import View
from .models import Medicine
import json

class MedicineView(View):
    def get(self, request):
        data = list(Medicine.objects.values())
        return HttpResponse(json.dumps(data), content_type = "application/json")