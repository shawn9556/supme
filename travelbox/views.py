from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from travelbox.models import Travel_box

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'travelbox/travelbox.html')
    elif request.method =='POST':
        mk_box = Travel_box()
        # mk_box.id = request.POST['id']
        mk_box.accomdation = request.POST['accomdation']
        # mk_box.food = request.POST['food']
        # mk_box.activity = request.POST['activity']
        # mk_box.sightseeing = request.POST['sightseeing']
        mk_box.place_name = request.POST['place_name']
        mk_box.traffic = request.POST['traffic']
        mk_box.save()
    
        return render(request, 'travelbox/travelbox.html')

# def read(request):
#     if request.method == 'GET':
#         result = Travel_box.objects.get()

#         return render(request,'travelbox/travelbox.html', result)


    
def test(request):
    
    return render(request, 'travelbox/test.html')

def login(request):

    return render(request, 'travelbox/login.html')

def read(request, post_id):
    
    post = Travel_box.objects.get(id= post_id)

    context = {
        'post': post,
        
    }

    return render(request, 'travelbox/read_box.html', context)