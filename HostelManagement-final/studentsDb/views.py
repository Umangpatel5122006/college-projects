from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Complaint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout

def home(request):

    if request.method == 'POST':
        if 'home' in request.POST:
            return render(request, 'home.html')  
        if 'profile' in request.POST:
            return redirect('profile')
        elif 'facilities' in request.POST:
            return redirect('facilities')  
        elif 'complaints' in request.POST:
            return redirect('complaints')  
        elif 'rules' in request.POST:
            return redirect('rules')  
        elif 'contact' in request.POST:
            return redirect('contact')  
        elif 'reset' in request.POST:
            return redirect('reset')  

        

        elif 'logout' in request.POST:
            return render(request,'home.html',{'logout':True})  # Redirect to a logout view or homepage
    else:
        return render(request, 'home.html')  # Default page (Home)



def facilities(request):
    return render(request, 'fac.html')

def complaints(request):
    if request.method == 'POST':
        Full_Name = request.POST.get('name')
        Room_Number = request.POST.get('room')
        Complaint_Type = request.POST.get('type')
        Complaint_Details = request.POST.get('message')

        Complaint.objects.create(
            Full_Name = Full_Name,
            Room_Number = Room_Number,
            Complaint_Type = Complaint_Type,
            Complaint_Details = Complaint_Details
        )
        return render(request,'complaints.html',{'success':True})
    return render(request, 'complaints.html')

def rules(request):   
    return render(request, 'rule.html')
def reset(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        try:
            user = Student.objects.get(username=username,email= email, password=current_password)
            if(new_password == confirm_password):
                user.password = new_password
                user.save()
                return render(request, 'reset.html',{'success':True})
            else:
                return render(request,'reset.html',{'error1':True})
        except:
            return render(request,'reset.html',{'error2':True})

    return render(request, 'reset.html')

def contact(request):
    return render(request, 'contact.html')
    
def login(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')

        if user_type == 'admin':
            return redirect('/admin/login/')
        elif user_type == 'student':
            return redirect('student-login')
    return render(request, 'login.html')
def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            student = Student.objects.get(username=username, email=email, password=password)
            request.session['username'] = username
            request.session['password'] = password
            print("Login successful, username set in session:", username) 
            return render(request,'sign.html',{'success':True})
        except Student.DoesNotExist:
            return render(request,'sign.html',{'error':True})
    return render(request, 'sign.html')

    
        
def profile(request):
    username = request.session.get('username')
    password = request.session.get('password')
    print("Session Username:", username)  # 🔍 Debugging line

    if not username:
        print("login required")
        return render(request, 'pro.html',{'error':True})

    try:
        student = Student.objects.get(username=username,password = password)
        print("Student Found:", student)  # 🔍 Debugging line
        return render(request, 'pro.html', {'student': student})
    except Student.DoesNotExist:
        print("Student DNE")
        return render(request,'pro.html',{'error2':True})
    
