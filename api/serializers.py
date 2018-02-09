from rest_framework import serializers
from api.models import DummyModel

class DummySerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyModel
        fields = '__all__'
