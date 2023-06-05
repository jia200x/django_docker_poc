from django.db import models
from django.db.models.signals import pre_save
import requests
import urllib.parse
import json

OSM_URL = "https://nominatim.openstreetmap.org/search?q={0}&format=json"

class Reader(models.Model):
    address = models.CharField(max_length=255)
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
    deveui = models.CharField(max_length=16)

    @classmethod
    def pre_create(cls, sender, instance, raw=False, **kwargs):
        is_new = instance.pk is None
        if raw:
            return
        
        address = instance.address
        t = Reader.get_lat_lon(address)
        instance.lat = t[0];
        instance.lon = t[1];

    @staticmethod
    def get_lat_lon(address):
        url = OSM_URL.format(urllib.parse.quote_plus(address))
        req = requests.get(url)
        data = json.loads(req.content)[0]
        return (data["lat"], data["lon"])
i
class Tag(models.Model):
    pass

class Transaction(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

pre_save.connect(Reader.pre_create, Reader)
