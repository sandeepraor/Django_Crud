from django.urls import include,path
from . import views
urlpatterns = [
        
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:eid>', views.edit),  
    path('update/<int:eid>', views.update),  
    path('delete/<int:eid>', views.destroy),
    path('login/',views.user_login),
    path('vehicle_add/',views.vehicle_add),
    path('vehicle_delete/<int:id>' , views.vehicle_destroy),
    path('vehicle_get/',views.vehicle_get)
]