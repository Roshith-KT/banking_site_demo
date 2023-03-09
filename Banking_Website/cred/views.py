from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('buttonpage')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()

            return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")