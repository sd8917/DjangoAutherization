# DjangoAutherization
* This authentication based app in django2

### url.py main project
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),

]

```

### views.py
```

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
     #Check for the method
    if request.method == 'POST':
        # tAKING THE USERNAME AND PASSSWORD FROM THE DATABASE IF AVAILABLE
        username = request.POST['username']
        messages.info(request,username)  # FOR DISPLAYING THE MSG TO USER
        password = request.POST['password'] 

        #CHECK FOR THE THE AUTH
        user = auth.authenticate(username=username, password=password)

        #CHECK FOR USER PRESENCE
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


```

### url.py

```
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]

```

### For more reference visit follow:-

[Youtube](https://www.youtube.com/watch?v=iT15mk4y1iw&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau&index=26)

[django auth docs](https://docs.djangoproject.com/en/2.2/topics/auth/default/)
