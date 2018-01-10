from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm

# Create your views here.
def device_table(request):
    devices = Device.objects.all()
    return render(request, 'inventory/device_table.html', {'devices': devices})

def device_new(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_table')
    else:
        form = DeviceForm()
    return render(request, 'inventory/device_new.html', {'form': form})

def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if device:
        device.delete()
    return redirect('device_table')
