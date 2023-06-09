from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def lp(request):
    return render(request, 'lp.html')
@login_required(login_url='login') 
def home(request):
    return render(request, 'home.html')
def course(request):
    return render(request, 'course.html')
def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        mail = request.POST ['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email = mail).exists():
                messages.info(request, 'Email is already used')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name = fname, last_name = lname,email= mail, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect( 'register')
    else:        
     return render (request,"signup.html")
def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username = username,password=password)
       if user is not None:
          auth.login(request, user)
          return redirect('home')
       else:
          messages.info(request, 'credentials invalid')
          return redirect('register')
    else:
      return render (request,"login.html")
def logout(request):    
    auth.logout(request)
    return redirect('lp')
