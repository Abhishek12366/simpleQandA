from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from api.models import Questions


class QuestionForm(forms.ModelForm):

    class Meta:
        model=Questions
        fields=["title","description","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control border border-start-0 border-top-0 border-end-0"}),
            "description":forms.Textarea(attrs={"class":"form-control border border-start-0 border-top-0 border-end-0","rows":5}),
            "image":forms.FileInput(attrs={"class":"form-select"})

        }



class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()




