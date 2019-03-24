from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    request.session.clear()
    return render(request,"LoginReg/login.html")

def good(request):
    if not "id" in request.session:
        return redirect("/")
    return redirect("Display/LoadPage")

def reg(request):
    errors = User.objects.validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    if request.POST["password_reg"] == request.POST["confirm"]:
        encrypted = bcrypt.hashpw(request.POST["password_reg"].encode(), bcrypt.gensalt())
    if request.method == "POST":
        x = User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"], email=request.POST["email_reg"],password=encrypted)
    request.session["id"] = x.id
    return redirect("/good")

def login(request):
    errors = User.objects.login(request.POST)
    if not errors == True:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    request.session["id"] = User.objects.get(email = request.POST["email_login"]).id
    return redirect("/good")

def logout(request):
    request.session.clear()
    return redirect("/")


# Create your views here.
