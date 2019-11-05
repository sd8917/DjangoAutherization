# DjangoAutherization

* App to manage the autherizations in django

>First add your app in installed app in seetings.py

### url.py
```
path('accounts/',include('accounts.urls')),
```

### views.py

```
def register(request):
    return render(request, 'register.html')

```

### Templates structure

>templates/register.html

```
<body>
    <form action="register" method="post">
        {% csrf_token %}
        <input type="text" name="first_name" placeholder="first Name"><br>
        <input type="text" name="last_name" placeholder="Last Name"><br>
        <input type="text" name="username" placeholder="UserName"><br>
        <input type="email" name="email" placeholder="Email here .."><br>
        <input type="password" name="password1" placeholder="Enter the Password"><br>
        <input type="password" name="password2" placeholder="Comfirm Password"><br>

        <input type="submit">
    </form>
</body>

```

# After checking for the diiferent auth condition

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
                print("UserName taken")
            elif User.objects.filter(email=email).exists():
                print("email taken")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
                user.save();
                print('user created')

        else:
            print('Password Not matching ..')

        return redirect('index')

    else:
        return render(request, 'register.html')

```
