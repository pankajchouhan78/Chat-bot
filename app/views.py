from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def chatbot(request):
    return render(request, 'chatbot.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('/')
            except:
                error_message = "Error Creating Account"
                return render(request,"register.html",{'error_message':error_message})
        else:
            error_message = "password don't match"
            return render(request,"register.html",{'error_message':error_message})
    return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/login/')