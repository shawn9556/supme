from django.urls import path

from travelbox import views


app_name='travelbox'

urlpatterns = [
    path("supme/", views.index, name="travelbox"),
    path('test/', views.test),
    path('login/', views.login),
    path('read/<int:post_id>/', views.read)
]