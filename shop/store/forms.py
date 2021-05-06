from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Upload,Product
from django.forms import ModelChoiceField

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(
        label='ชื่อ',
        max_length=100,
        required=True)

    last_name=forms.CharField(
        label='นามสกุล',
        max_length=100,
        required=True)

    email=forms.EmailField(
        label='อีเมล',
        max_length=250,
        help_text='example@gmail.com')

    class Meta :
        model=User
        fields=('first_name' ,
        'last_name',
        'username',
        'email',
        'password1',
        'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name' ,
        'last_name' ,
        'username', 
        'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UploadFileForm(forms.ModelForm):
    name = forms.CharField(label='ชื่อไฟล์งาน',max_length=50)
    description = forms.CharField(label='คำอธิบาย',max_length=150)
   
    class Meta:
        model = Upload   
        fields =['name','description','category','typefile','inputfile','image']

    