from django import forms
from .models import *

class VegetableFruitForm(forms.ModelForm):
    class Meta:
        model = VegetableFruit
        fields = ( 'name', 'quantity', 'price', 'count')

class GroceryStapleForm(forms.ModelForm):
    class Meta:
        model = GroceryStaple
        fields = ( 'name', 'quantity', 'price', 'count')

class HouseholdItemForm(forms.ModelForm):
    class Meta:
        model = HouseholdItem
        fields = ( 'name', 'quantity', 'price', 'count')

class PersonalCareForm(forms.ModelForm):
    class Meta:
        model = PersonalCare
        fields = ( 'name', 'quantity', 'price', 'count')

class SnacksBeverageForm(forms.ModelForm):
    class Meta:
        model = SnacksBeverage
        fields = ( 'name', 'quantity', 'price', 'count')