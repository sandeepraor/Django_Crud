from django.urls import path,include
from .views import *

urlpatterns = [
    path('add_location',add_place),
    path('add_distance',add_fromto),
    path('get_route',all_places_routes)
]