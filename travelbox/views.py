from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect

from travelbox.models import Travel_box

# Create your views here.


def create(request):
    if request.method == 'GET':
        return render(request, 'travelbox/box_create.html')
    elif request.method =='POST':
        mk_box = Travel_box()
        # mk_box.id = request.POST['id']
        mk_box.accomdation = request.POST['accomdation']
        mk_box.food = request.POST['food']
        mk_box.activity = request.POST['activity']
        mk_box.sightseeing = request.POST['sightseeing']
        mk_box.place_name = request.POST['place_name']
        mk_box.traffic = request.POST['traffic']
        if request.FILES.get("image"):
            print('ok')
            mk_box.image = request.FILES['image']
            
        mk_box.save()
    
        return render(request, 'travelbox/box_create.html')


    
def read(request, post_id):
    
    post = Travel_box.objects.get(id= post_id)

    context = {
        'post': post,
        
        
    }

    return render(request, 'travelbox/read_box.html', context)

def read_all(request):
    
    post_list = Travel_box.objects.all()

    context = {
        'posts': post_list
        
    }

    return render(request, 'travelbox/read_box_list.html', context)

def box_update(request, post_id):
    if request.method =='GET':
            
        post =Travel_box.objects.get(id = post_id)
        context = {
            'post' : post
        }
        return render(request, "travelbox/box_update.html", context)


    elif request.method =='POST':
        target_post = Travel_box.objects.get(id = post_id)
        target_post.place_name = request.POST['place_name']
        target_post.traffic = request.POST['traffic']
        target_post.accomdation = request.POST['accomdation']
        target_post.food = request.POST['food']
        target_post.activity = request.POST['activity']
        target_post.sightseeing = request.POST['sightseeing']
        if request.FILES.get("image"):
            print('ok')
            target_post.image = request.FILES['image']
        target_post.save()
        
        return HttpResponseRedirect('/travelbox/read-all/')


def delete(request, post_id):
    if request.method == "GET":
        post = Travel_box.objects.get(id = post_id)
        context = {
            'post' : post
        }
        return render(request, 'travelbox/box_delete.html', context)
    elif request.method == 'POST':
        delete_post = Travel_box.objects.get(id = post_id)
        delete_post.delete()
        return HttpResponseRedirect('/travelbox/read-all/')


def mybox(request, post_id):
   
    read = Travel_box.objects.get(id = post_id)
    context = {
        'post': read,
              
    }
    return render(request, "travelbox/mybox.html", context)


