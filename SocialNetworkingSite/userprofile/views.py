from multiprocessing import context
from django.shortcuts import render
from .models import Userprofile
from karamel.models import UserInfo
# Create your views here.


#Setup profile
def setup(request):
    if request.method == "POST":
        profile = Userprofile()
        username = request.POST['uname']
        userinfo = UserInfo.objects.filter(username = username).first()
        profile.userinfo = userinfo
        profile.status = request.POST['status']
        profile.bio = request.POST['bio']
        profile.pic = request.FILES['profilepic']
        
        profile.save()
        context = {"profile" : profile}
    return render(request, "about.html", context)