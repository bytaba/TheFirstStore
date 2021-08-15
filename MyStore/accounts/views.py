from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
# Create your views here.

def login_view (request):
    if request.method == 'POST' :
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            login (request , user)
            return redirect('index:index')
    else :
        form = AuthenticationForm()
    return render( request , 'accounts/login.html' , {'form' : form} )


def signup_view (request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login( request , user)
            return redirect("index:index")
    else:
        form = UserCreationForm()
    return render(request , 'accounts/signup.html' , {'form' : form} )  
