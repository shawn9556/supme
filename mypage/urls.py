from django.urls import path
from mypage import views

app_name="mypage"

urlpatterns=[
    path("signup/", views.post_create, name="signup"),
    path("login/", views.post_login, name="login"),
    path("profile/",views.profile, name="profile"),
    path("update/",views.update, name="update"),
    path("contact/",views.contact, name="contact"),
    path("progress/",views.progress, name="progress"),    

]
