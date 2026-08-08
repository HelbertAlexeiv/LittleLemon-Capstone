from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemsView, SingleMenuItemView, msg

#urls examples with path

urlpatterns =[
    #path('', views.sayHello, name="hello")
    #path('', views.index, name='index'),
    path('message/', msg),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu'),
    path('menu/items', MenuItemsView.as_view(), name='menu_items'),
    path('api-auth-token/', obtain_auth_token)
]


