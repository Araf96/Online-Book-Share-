from django.contrib.auth.models import User
from django import forms
from .models import UserProfile,UserLibrary

class UserAccount(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']


class UserFormAccount(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']




class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['pro_pic','phone' ,'country', 'job', 'organization']



class UserLibraryForm(forms.ModelForm):
    class Meta:
        model = UserLibrary
        fields = ['book_name','author_name' ,'category', 'publishing_year', 'book_image']


