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
        <input type="email" name="email" placeholder="Email here .."><br>
        <input type="password" name="password1" placeholder="Enter the Password"><br>
        <input type="password" name="password2" placeholder="Comfirm Password"><br>

        <input type="submit">
    </form>
</body>

```
