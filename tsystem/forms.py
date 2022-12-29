from django import forms  
from tsystem.models import Employee  , Login , Vehicle
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__" 
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"