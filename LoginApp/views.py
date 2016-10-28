from django.shortcuts import render, redirect

# Create your views here.
from LoginApp.forms import LoginForm


def login_page(request):
    newForm = LoginForm()
    if request.method != 'POST':
        return render(request, "LoginApp/login.html", {'form': newForm})
    else:
        return redirect("LoginApp:main")