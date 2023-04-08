from django import forms
from .models import AddStuble



class AddStubleform(forms.ModelForm):
    class Meta:
        model=AddStuble
        fields="__all__"
        exclude = ["aadhar_number"]
        


