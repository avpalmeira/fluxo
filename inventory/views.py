from django.shortcuts import render
from .models import Device

# Create your views here.
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'inventory/device_table.html', {'devices': devices})

