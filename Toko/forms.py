from django import forms
from .models import Toko

class TokoForm(forms.ModelForm):

    class Meta :
        model = Toko
        fields = '__all__'