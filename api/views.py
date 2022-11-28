
from api.models import Answers, Questions

# Create your views here.
from api.serializers import QuestionSerializers, UserSerilalizer,AnswerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.models import Questions
from rest_framework import authentication,permissions
from rest_framework.decorators import action 

class UsersView(ModelViewSet):
    serializer_class=UserSerilalizer
    queryset=User.objects.all()

class QuestionsView(ModelViewSet):
    serializer_class=QuestionSerializers
    queryset=Questions.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_class=[permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    @action(methods=["GET"],detail=False)
    def my_question(self,request,*args,**kw):
        qs=request.user.questions_set.all()
        serializer=QuestionSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    @action(methods=["POST"],detail=True)
    def add_answer(self,request,*args,**kw):
        id=kw.get("pk")
        ques=Questions.objects.get(id=id)
        usr=request.user
        serializer=AnswerSerializer(data=request.data,context={"question":ques,"user":usr})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    @action(methods=["GET"],detail=True)
    def list_answers(self,request,*args,**kw):
        id=kw.get("pk")
        ques=Questions.objects.get(id=id)
        qs=ques.answers_set.all()
        serializer=AnswerSerializer(qs,many=True)
        return Response(data=serializer.data)

class AnswersView(ModelViewSet):
    serializer_class=AnswerSerializer
    queryset=Answers.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=['GET'],detail=True)
    def upvote(self,request,*args,**kw):
        ans=self.get_object()
        usr=request.user
        ans.upvote.add(usr)
        return Response(data="created")
        