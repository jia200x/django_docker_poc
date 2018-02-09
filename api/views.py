from django.shortcuts import render
from api.models import DummyModel
from api.serializers import DummySerializer
from rest_framework import viewsets

# Create your views here.

class DummyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DummyModel.objects.all()
    serializer_class = DummySerializer
