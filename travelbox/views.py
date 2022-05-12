from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect

from travelbox.models import GetPic, Travel_box, City
import requests
from .forms import CityForm

# Create your views here.


def create(request):
    if request.method == 'GET':
        return render(request, 'travelbox/box_create.html')
    elif request.method =='POST':
        mk_box = Travel_box()
        # mk_box.id = request.POST['id']
        mk_box.sub_title = request.POST.get('sub_title')
        mk_box.script = request.POST.get('script')
        mk_box.place_name = request.POST.get("place_name")
        mk_box.activity = request.POST.get('activity')
        mk_box.accomdation = request.POST.get('accomdation')
        mk_box.food = request.POST.get('food')      
        mk_box.sightseeing = request.POST.get('sightseeing')      
        mk_box.traffic = request.POST.get('traffic')

        if request.FILES.get("image_head"):          
            mk_box.image_head = request.FILES['image_head']
        if request.FILES.get("image_1"):          
            mk_box.image_1 = request.FILES['image_1']
        if request.FILES.get("image_2"):  
            mk_box.image_2 = request.FILES['image_2']
        if request.FILES.get("image_3"):  
            mk_box.image_3 = request.FILES['image_3']

        if mk_box.place_name == "none":
            return redirect("travelbox:create")   
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
        if request.FILES.get("image_1"):
            print('ok')
            target_post.image_1 = request.FILES['image_1']
        if request.FILES.get("image_2"):
            print('ok')
            target_post.image_2 = request.FILES['image_2']
        if request.FILES.get("image_3"):
            print('ok')
            target_post.image_3 = request.FILES['image_3']
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

    if request.method =='POST':
        print("here")
    
        get_pic = GetPic()
        get_pic.box_id = read

        if request.FILES.get("user_image_1"):          
            get_pic.user_image_1 = request.FILES['user_image_1']
        if request.FILES.get("user_image_2"):  
            get_pic.user_image_2 = request.FILES['user_image_2']
        if request.FILES.get("user_image_3"):  
            get_pic.user_image_3 = request.FILES['user_image_3']

        
        get_pic.save()

        return render(request, "travelbox/mybox_submit_results.html", {
            "success": True,
        })

        # return redirect("travelbox:home")

    return render(request, "travelbox/mybox.html", context)
   


def weather(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5054f8884263db59d70b67fc83db029e'

    cities = City.objects.all() #return all the cities in the database
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save()
    
    form = CityForm()
    weather_data = []


    for city in cities:
        response = requests.get(url.format(city))
        if response.status_code != 200:
            print(city)
            continue
        city_weather = response.json() #request the API data and convert the JSON to Python data types
        print(f"city: {city}")
        # for key, value in city_weather.items():
        #     print(f"{key}: {value}")

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'travelbox/weather.html', context) #returns the index.html te


def home(request):
    return render(request,  'travelbox/home.html')

    
def test(request, post_id):
    read = Travel_box.objects.get(id = post_id)
    context = {
        'post': read,
    }

    if request.method =='POST':
        print("here")
    
        get_pic = GetPic()
        get_pic.box_id = read

        if request.FILES.get("user_image_1"):          
            get_pic.user_image_1 = request.FILES['user_image_1']
        if request.FILES.get("user_image_2"):  
            get_pic.user_image_2 = request.FILES['user_image_2']
        if request.FILES.get("user_image_3"):  
            get_pic.user_image_3 = request.FILES['user_image_3']
        get_pic.save()

        return render(request, "travelbox/mybox_submit_results.html", {
            "success": True,
        })

        # return redirect("travelbox:home")

    return render(request, "travelbox/index.html", context)

def test2(request, post_id):
    read = Travel_box.objects.get(id = post_id)
    context = {
        'post': read,
    }

    if request.method =='POST':
        print("here")
    
        get_pic = GetPic()
        get_pic.box_id = read

        if request.FILES.get("user_image_1"):          
            get_pic.user_image_1 = request.FILES['user_image_1']
        if request.FILES.get("user_image_2"):  
            get_pic.user_image_2 = request.FILES['user_image_2']
        if request.FILES.get("user_image_3"):  
            get_pic.user_image_3 = request.FILES['user_image_3']
        get_pic.save()

        return render(request, "travelbox/mybox_submit_results.html", {
            "success": True,
        })

      

    return render(request, "travelbox/test_2.html", context)
    