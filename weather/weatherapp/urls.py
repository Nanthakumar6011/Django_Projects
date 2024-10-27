from django.urls import path
from .import views


urlpatterns = [
      
    path('',views.weather,name='weather'),
    path('delete/<CName>',views.delete_city,name='Dcity'),
]