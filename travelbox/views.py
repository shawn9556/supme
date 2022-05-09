from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect

from travelbox.models import GetPic, Travel_box

# Create your views here.


def create(request):
    if request.method == 'GET':
        return render(request, 'travelbox/box_create.html')
    elif request.method =='POST':
        mk_box = Travel_box()
        # mk_box.id = request.POST['id']
        mk_box.accomdation = request.POST.get('accomdation')
        mk_box.food = request.POST.get('food')
        mk_box.activity = request.POST.get('activity')
        mk_box.sightseeing = request.POST.get('sightseeing')
        mk_box.place_name = request.POST['place_name']
        mk_box.traffic = request.POST.get('traffic')
        if request.FILES.get("image_1"):          
            mk_box.image_1 = request.FILES['image_1']
        if request.FILES.get("image_2"):  
            mk_box.image_2 = request.FILES['image_2']
        if request.FILES.get("image_3"):  
            mk_box.image_3 = request.FILES['image_3']
            
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

    # if request.method =='POST':
    
    #     get_pic = GetPic()

    #     if request.FILES.get("user_image_1"):          
    #         get_pic.user_image_1 = request.FILES['user_image_1']
    #     if request.FILES.get("user_image_2"):  
    #         get_pic.user_image_2 = request.FILES['user_image_2']
    #     if request.FILES.get("user_image_3"):  
    #         get_pic.user_image_3 = request.FILES['user_image_3']

    return render(request, "travelbox/mybox.html", context)


# def getpic(request, post_id):
   
#    post = GetPic().objects.get(id= post_id)

#    context = {
#         'post': post,
        
        
#     }



#    return render(request, "travelbox/user_pic.html", context)

def user_pic_create(request):
    if request.method == 'GET':
        return render(request, 'travelbox/mybox.html')
    elif request.method =='POST':
        get_pic = GetPic()
        # mk_box.id = request.POST['id']
     
        if request.FILES.get("user_image_1"):          
            get_pic.user_image_1 = request.FILES['user_image_1']
        if request.FILES.get("user_image_2"):  
            get_pic.user_image_2 = request.FILES['user_image_2']
        if request.FILES.get("user_image_3"):  
            get_pic.user_image_3 = request.FILES['user_image_3']
            
        get_pic.save()
    
        return render(request, 'travelbox/user_pic.html')

def read_pic(request, post_id):
    
    post = GetPic.objects.get(id= post_id)

    context = {
        'post': post,
        
        
    }

    return render(request, 'travelbox/read_box.html', context)
