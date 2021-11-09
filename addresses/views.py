from django.shortcuts import render
from .models import Address

# Create your views here.

def mapPage(request):
    addresses = Address.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoibG9naWMtcHJvIiwiYSI6ImNrdjU2NGNkNDB1b28yb3BoMmY2bmE5aWIifQ.xyQXGpJg8S8n7JAD3KSPQg'
    return render(request, 'addresses/map.html', context={'addresses': addresses, 'mapbox_access_token': mapbox_access_token})