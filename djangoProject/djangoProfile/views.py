from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'djangoProfile/register.html', {'form': form})

def login(request):
    return render(request, 'djangoProfile/login.html')

@login_required
def profile(request):
    return render(request, 'djangoProfile/profile.html')