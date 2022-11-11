import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.
class  Questions(models.Model):
    title=models.CharField(max_length=300)
    description=models.CharField(max_length=350)
    image=models.ImageField(upload_to="images",null=True)
    created_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    @property
    def question_answers(self):
        qs=self.answers.set.all().annotate(u_count=Count('upvote').order_by("-u_count"))
        return qs
        #return self.answers_set.all()

    def __str__(self):
        return self.title
class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    upvote=models.ManyToManyField(User,related_name="upvote")
    created_date=models.DateField(auto_now_add=True)


    def __str__(self) :
        return self.answer

    @property
    def votecount(self):
        return self.upvote.all().count()

#python manage.py create super user
#from api.models import Questions,Answers
#usr.questions_set.create("title",description="angular architeture?)
# usr.questions_set.all()