from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
@require_http_methods(['POST','GET'])
def signup(request):
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_voted=False
            user.save()
            # return
            return redirect('questions:index')
    else:
        form = CustomUserCreationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['POST','GET'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('questions:index')
    else:
        form=AuthenticationForm(request)
    context={'form':form,}
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('questions:index')