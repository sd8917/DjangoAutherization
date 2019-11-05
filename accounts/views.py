from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName taken')
                return redirect('register')
                # print("UserName taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                # print("email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
                user.save();
                print('user created')

        else:
            print('Password Not matching ..')
            return redirect('register')

        return redirect('index')

    else:
        return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        messages.info(request,username)
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            print("user is logged in")
            return redirect('index')

        else:
            messages.info(request,'invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
