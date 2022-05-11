from django.urls import path

from travelbox import views


app_name='travelbox'

urlpatterns = [
    path("create/", views.create, name="create"),
    path('read/<int:post_id>/', views.read, name='read_box'),
    path('read-all/', views.read_all, name='read_all'),
    path('update/<int:post_id>/', views.box_update, name='box_update'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('mybox/<int:post_id>/', views.mybox, name='mybox'),
    path('weather/', views.weather, name='weather'),
    path('home/', views.home, name='home'),
    path('test/<int:post_id>/', views.test, name='test'),

]