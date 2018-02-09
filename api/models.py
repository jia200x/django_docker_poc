from django.db import models

# Create your models here.
class DummyModel(models.Model):
    dummy_field = models.CharField(max_length=32)
