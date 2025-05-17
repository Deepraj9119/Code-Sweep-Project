from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to your home page url name
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists.'})
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')  # Change 'home' to your home page url name
    return render(request, 'signup.html')

@login_required
def profile_view(request):
    user = request.user
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        # Update user fields
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return render(request, "profile.html", {"user": user})
