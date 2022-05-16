from django.shortcuts import render

# Create your views here.
from mypage.models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def post_create(request):
    if request.method=="GET":
        return render(request, "mypage/signup.html")
    elif request.method =="POST":
        new_post=Post()
        new_post.name=request.POST["name"]
        new_post.nickname=request.POST["nickname"]
        new_post.phonenumber=request.POST["phonenumber"]
        new_post.emailadress=request.POST["emailadress"]
        new_post.adresshome=request.POST["adresshome"]   
        new_post.save()
        return HttpResponseRedirect(reverse("mypage:login"))


def post_login(request):
    post_list = Post.objects.all()
    context = {
        "posts": post_list
    }
    return render(request,"mypage/login.html",context)


def profile(request):
    return render(request, "mypage/profile.html")

def update(request):
    return render(request, "mypage/update.html")



def contact(request):
    return render(request,"mypage/contact.html")


def progress(request):
    return render(request,"mypage/progress.html")


def sample(request):
    return render(request,"mypage/sample.html")    

def profile_tmp(request):
    return render(request,"mypage/profile_tmp.html")   