from django.urls import path,include
from .views import *

urlpatterns = [
    path('add_location',add_place),
    path('add_distance',add_fromto),
    path('get_route',all_places_routes),
    path('travel_book',book_trip),
    path('getplace/<str:frm>',getloacation),
    path('getdistance/<str:frm>/<str:to>',getdistance),
    path('getvehicleprice/<str:regno>',getvehicleprice)
]