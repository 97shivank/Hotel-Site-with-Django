from django import forms
from .models import Reserve , Property


class ReserveForm(forms.ModelForm):
    class Meta:
        model=Reserve
        fields='__all__'

#class PropertySearch(forms.ModelForm):
  #  class Meta:
   #     model= Property
        