from django import forms
from .models import UrineStripImage


class UrineStripImageForm(forms.ModelForm):
    class Meta:
        model = UrineStripImage
        fields = ("image",)
