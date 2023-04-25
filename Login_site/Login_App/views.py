from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def Home(request):
    return render(request, 'Home.html')


def Loginpage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/home')
        else:
            messages.error(request, "Invalid Credentails")
            return redirect('/login')

    return render(request, 'Login.html')


def Signuppage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        conformpassword = request.POST.get('pass2')

        if password != conformpassword:
            messages.warning(request, "Password is Incorrect")
            return redirect('/signup')

        try:
            if User.objects.get(username=uname):
                messages.info(request, "Username is already taken")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email is already taken")
                return redirect('/signup')
        except:
            pass

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "Signup Success Please Login!")
        return redirect('/login')

    return render(request, 'signup.html')


def Profile(request):
    return render(request, 'profile.html')


def logoutpage(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/login')
