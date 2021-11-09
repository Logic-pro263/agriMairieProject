from django.db import models
import geocoder


# Create your models here.

mapbox_access_token = 'pk.eyJ1IjoibG9naWMtcHJvIiwiYSI6ImNrdjU2NGNkNDB1b28yb3BoMmY2bmE5aWIifQ.xyQXGpJg8S8n7JAD3KSPQg'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Address'


    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
    def __str__(self):
        return self.address