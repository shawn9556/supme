from django.urls import path

from travelbox import views


app_name='travelbox'

urlpatterns = [
    path("supme/", views.index)
]