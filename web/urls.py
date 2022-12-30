from django.urls import path
from .views import SignInView,SignUpView,IndexView
urlpatterns = [
    path("",SignInView.as_view(),name="signin"),
    path("register",SignUpView.as_view(),name="signup"),
    path("index",IndexView.as_view(),name="index")
]
