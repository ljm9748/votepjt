from django import forms
from .models import Comment,Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('title','first_question','second_question',)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)
    