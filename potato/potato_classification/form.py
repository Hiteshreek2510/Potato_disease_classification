from .models import Image
from django import forms
class Imageform(forms.ModelForm):
    class Meta:
        model=Image
        fields=['caption','image']