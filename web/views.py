from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import CreateView,FormView,TemplateView,ListView
from .forms import LoginForm,UserRegistrationForm,QuestionForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login
from api.models import Questions


class SignUpView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    success_url=reverse_lazy("signin")
    

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self, request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,self.template_name,{"form":form})

class IndexView(CreateView,ListView):
    template_name="index.html"
    form_class=QuestionForm
    success_url=reverse_lazy("index")
    model=Questions
    context_object_name="questions"

    def form_valid(self, form) :
        form.instance.user=self.request.user       
        messages.success(self.request,"your question added successfully")
        return super().form_valid(form)
    def get_queryset(self):
        return Questions.objects.exclude(user=self.request.user).order_by("-created_date")



