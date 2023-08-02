from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('courses')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('rememberMe')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(3600)
            else:
                request.session.set_expiry(0)
            return redirect('courses')
        else:

            messages.error(request, 'Username or Password does not exist')

    context = {'page': page}
    return render(request, 'base/loginPage.html', context)

def courses(request):
    return render(request, 'base/courses.html' )


def profile(request):
    return render(request, 'base/profile.html' )

def editProfile(request):
    return render(request, 'base/editProfile.html')

def logoutUser(request):
    logout(request)
    return redirect('login')