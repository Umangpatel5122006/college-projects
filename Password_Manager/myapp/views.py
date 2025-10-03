from django.shortcuts import render,redirect
from .models import Credential
from .forms import CredentialForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_credential(request):
    if request.method == 'POST':
        site = request.POST.get('site')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Credential.objects.create(
            user=request.user,
            site=site,
            username=username,
            email=email,
            password=password
        )
        return redirect(f"{reverse('thank-you')}?site={site}")

    return render(request, 'vault/add.html')

# Sign Up View
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'vault/signup.html')

#Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'vault/login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')




def home(request):
    return render(request, 'vault/home.html')




def thank_you(request):
    site = request.GET.get('site', '')
    return render(request, 'vault/thank.html')


@login_required
def search_credential(request):
    query = request.GET.get('q', '')
    
    credentials = Credential.objects.filter(
        user=request.user  
    ).filter(
        site__icontains=query
    ) | Credential.objects.filter(
        user=request.user,
        username__icontains=query
    ) | Credential.objects.filter(
        user=request.user,
        email__icontains=query
    ) | Credential.objects.filter(
        user=request.user,
        password__icontains=query
    )
    return render(request, 'vault/search.html', {'credentials': credentials})

@login_required
def delete_credential(request, credential_id):
    try:
        credential = Credential.objects.get(id=credential_id, user=request.user)  # credential belongs to the logged-in user
        credential.delete()
        messages.success(request, "Credential deleted successfully!")
    except Credential.DoesNotExist:
        messages.error(request, "Credential not found or you don't have permission to delete it.")
    return redirect('search')  # Redirect back to the search page
