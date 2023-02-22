from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>', views.menu_item, name='menu_item'),
]