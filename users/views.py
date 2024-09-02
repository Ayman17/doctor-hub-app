from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# signup view function
def user_signup(request):
    # check request is post or get
    notvalidInfo = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            notvalidInfo = True
    form = SignUpForm()
    return render(request, 'users/signup.html', {'form' : form, 'notValidInfo' : notvalidInfo})
    
# login view function
def user_login(request):
    userNotExist = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                userNotExist = True
        else:
            userNotExist = True
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form' : form, 'userNotExist' : userNotExist})

# logout view function   
def user_logout(request):
    logout(request)
    return redirect('login')

# Display user profile
def user_profile(request): 
    print(f'User: {request.user}')
    return render(request, 'users/user_profile.html', {'user' : request.user})