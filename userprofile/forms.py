from django import forms 
# from django.contrib.auth.forms import ModelForm
from django.forms import ModelForm
from userprofile.models import *
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'pix', 'email', 'address', 'phone', 'dob', 'nationality', 'gender']

        GENDER = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('others', 'others'),
        ]

        STATE = [
            ('Enugu', 'Enugu'),
            ('Delta', 'Delta'),
            ('Ekiti', 'Ekiti'),
            ('Ogun', 'Ogun'),
            ('Lagos', 'Abia'),
            ('Abia', 'Abia'),
            ('Akwa-Ibom', 'Akwa-Ibom'),
            ('Imo', 'Imo'),
        ]
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'pix': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Image'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'dob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}, choices= GENDER),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'State'}, choices= STATE),
        }