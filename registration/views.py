from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    instance = get_object_or_404(UserProfile,user= request.user)
    profile_update_form = UserProfileForm(request.POST or None,request.FILES or None,instance=instance)
    if profile_update_form.is_valid():
        profile_update_form.save()
    return render(request, 'profile.html', {'profile':profile_update_form,'details':instance})


