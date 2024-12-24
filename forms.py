from django import forms
from .models import *

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ('name', 'img', 'description')  # Corrected field names to match your model
