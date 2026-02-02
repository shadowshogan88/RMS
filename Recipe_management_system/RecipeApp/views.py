from django.shortcuts import render,redirect
from django.contrib import messages
from RecipeApp.models import *
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        user_exists = AuthUserModel.objects.filter(username=username).exists()
        
        if user_exists:
            messages.warning(request, 'User already exists.')
            return redirect('sign_up')
        
        if password == confirm_password:
            AuthUserModel.objects.create_user(
                username=username,
                password=password,
                email=email,
                user_role = 'Admin',
            )
            messages.success(request, 'Account Successfully created.')
            return redirect('sign_in')
        else:
            messages.warning(request, 'Both password not matched.')
            return redirect('sign_up')
    
    return render(request, 'pages/sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, 'Welcome To your Dashboard.')
            return redirect('profile')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('sign_in')
    
    
    return render(request, 'pages/login2.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Log Out Sucessful!')
    return redirect("index")


def change_pass(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.warning(request, 'Both passwords do not match.')
            return redirect('change_pass')

        user = request.user
        user.set_password(password) 
        user.save()

        # update_session_auth_hash(request, user)

        messages.success(request, 'Password successfully changed.')
        return redirect('dashboard')

    return render(request, 'change_pass.html')

# 
def profile(request):
    
    return render(request, 'pages/my_profile.html')

def index(request):
    
    return render(request, 'pages/index.html')

def all_recipe(request):

    return render(request, 'pages/all_recipe.html')

def blog(request):

    return render(request,'pages/blog.html')

def contact(request):
    return render(request, 'pages/contact.html')

