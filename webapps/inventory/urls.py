from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('item-page', views.item_page, name='item-page'),

]