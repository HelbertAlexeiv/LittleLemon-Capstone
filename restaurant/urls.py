from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MenuItemsView, SingleMenuItemView

#urls examples with path

urlpatterns =[
    #path('', views.sayHello, name="hello")
    path('', views.index, name='index'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu'),
    path('menu/items', MenuItemsView.as_view(), name='menu_items'),
]


