from django.shortcuts import render,redirect,get_object_or_404
from .forms import CommentForm,QuestionForm
from .models import Question
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.decorators import login_required

def index(request):
    # questions=Question.objects.all()
    question=get_object_or_404(Question, pk=1)
    first_rate=question.first_count / (question.first_count+question.second_count) * 100
    second_rate = 100 - first_rate
    comment_form=CommentForm()
    context={
        'question':question,
        'comment_form':comment_form,
        'first_rate': first_rate,
        'second_rate' : second_rate,
    }
    return render(request, 'questions/index.html', context)

@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.user=request.user
            question.first_count=0
            question.second_count=0
            question.save()
            return redirect('questions:index')
    else:
        form=QuestionForm()
    context={
        'form':form,
    }
    return render(request, 'questions/create.html', context)

@require_POST
def create_comment(request, pk):
    if request.method == 'POST':
        question=get_object_or_404(Question, pk=pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.question=question
            comment.save()
            return redirect('questions:index')

@require_http_methods(['POST','GET'])
def update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        question=form.save()
        return redirect('questions:index')
        
    else:
        form = QuestionForm(instance=question)
    context={
        'form':form,
    }
    return render(request, 'questions/update.html', context)

def pick(request, pk , pick_num):
    question = get_object_or_404(Question, pk=pk)
    user=request.user
    if user.is_voted == 0:
        if pick_num == 1:
            tmp = question.first_count +1
            question.first_count = tmp
            user.is_voted = True
            user.save()
        elif pick_num ==2:
            tmp = question.second_count +1
            question.second_count = tmp
            user.is_voted = True
            user.save()
        question.save()
    return redirect('questions:index')
    
        
