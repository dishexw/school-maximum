from django import forms
from django.core import validators



class AdvertisementForm(forms.Form):
    first_name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}), validators=[validators.validate_slug])
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg'}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-lg'}))


