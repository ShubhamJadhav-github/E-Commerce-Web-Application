from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('about', views.about),
    path('products', views.products_function),
    path('contact', views.contact),
    path('login', views.login),
    path('buy', views.buy),
]