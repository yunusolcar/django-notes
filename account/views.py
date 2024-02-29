from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("homepage")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request, "account/login.html",{"error": "username or password wrong!"})


    return render(request,"account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["name"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request, "account/register.html",{"error": "username already using!", "username": username, "email": email, "name": name, "lastname": lastname})
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, "account/register.html",{"error": "email already using!", "username": username, "email": email, "name": name, "lastname": lastname})
                else:
                    user = User.objects.create_user(username = username, email = email, password = password, first_name= name, last_name = lastname)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html",{"error": "password not matching!", "username": username, "email": email, "name": name, "lastname": lastname})



    return render(request,"account/register.html")

def logout_request(request):
    logout(request)
    return redirect("homepage")