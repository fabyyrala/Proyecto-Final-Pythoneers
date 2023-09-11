from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from apps.user.forms import NewUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UpdateAvatarForm
from django.contrib.auth.models import Group

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = NewUserProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='registered_user')
            user.groups.add(group)
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username') #claned_data sirve para obtener los datos del formulario
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                print('te logueaste')
                return redirect('index')
    context = {
        'form': form
    } 
    return render(request, 'auth/login.html', context)

def logoutUser(request):
    logout(request)
    print('te deslogueaste')
    return redirect('index')

def profile(request, id):
    user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(UserProfile, pk=id)
    form = UpdateAvatarForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save()
            return redirect('user:profile', profile.id)
    context = {
        'user': user,
        'updateAvatarForm': form
    }
    return render(request, 'user/profile.html', context)
    

#controlar si funciona xd
def changePassword(request):
    user = request.user
    form = PasswordChangeForm(data=request.POST or None, user=user)
    if request.method == "POST":
        if form.is_valid():
            password = form.cleaned_data.get('new_password1')
            user.set_password(password)
            user.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'auth/changePassword.html', context)