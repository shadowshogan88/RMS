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
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            messages.warning(request, 'Name, email, and message are required.')
            return redirect('contact')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )
        messages.success(request, 'Message sent successfully.')
        return redirect('contact')

    return render(request, 'pages/contact.html')


def submit_recipe(request):
    categories = CategoryModels.objects.all().order_by('name')
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        preparation_time = request.POST.get('preparation_time', '').strip()
        cooking_time = request.POST.get('cooking_time', '').strip()
        difficulty = request.POST.get('difficulty', '').strip()
        serves = request.POST.get('serves', '').strip()
        category_id = request.POST.get('category')
        description = request.POST.get('description', '').strip()
        ingredients = request.POST.get('ingredients', '').strip()
        instructions = request.POST.get('instructions', '').strip()
        status = request.POST.get('status', Recipe.STATUS_WORKING)
        photo = request.FILES.get('photo')

        if not title or not description or not ingredients or not instructions:
            messages.warning(request, 'Please fill in all required fields.')
            return redirect('submit_recipe')

        category = None
        if category_id:
            category = CategoryModels.objects.filter(id=category_id).first()

        Recipe.objects.create(
            title=title,
            preparation_time=preparation_time,
            cooking_time=cooking_time,
            difficulty=difficulty,
            serves=serves,
            category=category,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            status=status,
            photo=photo,
        )
        messages.success(request, 'Recipe submitted successfully.')
        return redirect('submit_recipe')

    return render(request, 'pages/submit_recipe.html', {'categories': categories})


def category_list(request):
    categories = CategoryModels.objects.all().order_by('name')
    return render(request, 'pages/category_list.html', {'categories': categories})

