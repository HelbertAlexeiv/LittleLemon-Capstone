from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
# Create your views here.

#Examples views
def sayHello(request):
    return HttpResponse("Hello World")

def index(request):
    return render(request, 'index.html', {})

#-------app views------
class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer