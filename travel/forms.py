from django import forms
from .models import Location,Distance,BookTrip

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
class DistanceForm(forms.ModelForm):
    class Meta:
        model = Distance
        fields = "__all__"


class TripForm(forms.ModelForm):
    class Meta:
        model = BookTrip
        fields = '__all__'