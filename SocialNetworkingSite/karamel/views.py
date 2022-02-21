from operator import ge
import re
from django.shortcuts import render
from cryptography.fernet import Fernet

from karamel.models import UserInfo
# Create your views here.



def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def about(request):
    return render(request, "about.html")

#Register the User

def register(request):

    #Fetching all data comming from post method
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    dob = request.POST['dob']
    gender = request.POST['gender']
    username = request.POST['uname']
    password = request.POST['pass']
    conform_password = request.POST['cpass']

    #Compair Passwords
    if password != conform_password:
        return render(request, "signup.html", {"pass_error": "Password and Conform Password is not matching"})
    
    #duplicate username check
    if UserInfo.objects.filter(username = username).exists():
        return render(request, "signup.html", {"duplicate_user": "This username is already taken please try diffrent username"})

    #Add to the database
    userinfo = UserInfo.objects.create(name = name, email = email, mobile = mobile, gender = gender, dob = dob, username = username, password = password)
    userinfo.save()
    return render(request, "setup.html", {"username": username})

#Authenticate
def auth(request):
    #Method Check
    if request.method == "POST":
        #Fetching Data
        username = request.POST['uname']
        password = request.POST['pass']


        #Database Check
        if UserInfo.objects.filter(username = username, password = password):
            return render(request, "about.html")

        else:
            return render(request, "login.html", {"login_error":"Username or Password Incorrect"})