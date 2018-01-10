from django import forms

from .models import Device

class DeviceForm(forms.ModelForm):

    class Meta:
       model = Device
       fields = (
               'product_name',
               'reference_code',
               'category',
               'owner',
               'location',
               'sell_value',
               'buy_value'
               )
