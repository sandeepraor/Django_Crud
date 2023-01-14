from django import forms
from .models import Location,Distance

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
class DistanceForm(forms.ModelForm):
    class Meta:
        model = Distance
        fields = "__all__"