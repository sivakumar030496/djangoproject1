from .views import *
from django.urls import path


urlpatterns = [
    path('index/', index),
    path('register/', register),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('delete1/<int:id>', delete),
    path('login/', login),
    path('logout/', logout),
    path('send_mail/<str:email>', send_mail),
    path('home/',home),
    path('queries/',queriesql)
 ]