from django.urls import path
from .views import SigninView,SignupView,IndexView,add_answer,answer_upvote


urlpatterns = [
    path("login",SigninView.as_view(),name="signin"),
    path("index",IndexView.as_view(),name="index"),
    path("register",SignupView.as_view(), name="signup"),
    path("question/<int:id>/answer/add",add_answer,name="add-answer"),
    path("answers/<int:id>/upvote/add",answer_upvote,name="add-upvote"),
   
]
