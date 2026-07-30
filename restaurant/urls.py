from django.urls import path
from . import views

urlpatterns =[
    #path('', views.sayHello, name="hello")
    path('', views.index, name='index'),
]