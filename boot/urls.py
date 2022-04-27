from django.shortcuts import render
from django.urls import path ##path->8번으로 간다!

from boot import views

app_name = "boot"
urlpatterns = [
    path("base/", views.test),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("home/", views.index, name="home"),
    path("inquiry/create/", views.inquiry_create),
    path("login/", views.login, name="login"),
    path("sign-up/", views.sign_up, name="sign_uo"),
    path("logout/", views.logout, name="logout"),
    
]