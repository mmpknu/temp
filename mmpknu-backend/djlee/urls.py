from django.urls import path

from . import views

urlpatterns = [
    path('nearstore/<gpsx>/<gpsy>/', views.get_list_near_store),
    path('nearplace/<gpsx>/<gpsy>/', views.get_list_near_place), 
]
