from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import Questions
 

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=['title','description','image']

class Userregisterform(UserCreationForm):
     class Meta:
        model=User
        fields=["first_name","last_name","username","password1","email","password2"]
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()