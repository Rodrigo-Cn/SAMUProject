import base64
from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    medicine_image = serializers.SerializerMethodField()

    def get_medicine_image(self, obj):
        if obj.medicine_image:
            with open(obj.medicine_image.path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        return None

    class Meta:
        model = Medicine
        fields = ["id", "name", "dosage", "manufacturer", "medicine_image"]
