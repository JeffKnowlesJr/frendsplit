from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout as auth_logout

def index(request):
    return render(request, 'frendsplitapp/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'frendsplitapp/signup.html', {'form': form})

def learn_more(request):
    return render(request, 'frendsplitapp/learn_more.html')

def logout(request):
    auth_logout(request)
    return redirect('index')