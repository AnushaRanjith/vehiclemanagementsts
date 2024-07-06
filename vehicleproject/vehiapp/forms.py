from django import forms
from django.contrib.auth.models import User
from vehiapp.models import VehiModel

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=VehiModel
        exclude=['user','status']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model=VehiModel
        exclude=['user',]

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.CheckboxInput(attrs={'class':'form-check-input'})

        }


