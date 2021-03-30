from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=200)
    first_question=models.CharField(max_length=200)
    second_question=models.CharField(max_length=200)
    first_count=models.IntegerField()
    second_count=models.IntegerField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Comment(models.Model):
    content=models.CharField(max_length=300)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    
