from django.urls import include,path
from . import views
urlpatterns = [
    path('vehicle_add/',views.vehicle_add),
    path('vehicle_delete/<str:id>' , views.vehicle_destroy),
    path('vehicle_get/',views.vehicle_get),
    path('vehicle_update/<str:id>',views.vehicle_update),
    path('vehicle_edit/<str:id>',views.vehicle_edit)
]