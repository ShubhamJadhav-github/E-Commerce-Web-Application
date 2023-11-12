from django.urls import path
from loggedin import views
urlpatterns = [
    path('loggedin', views.index)
]
