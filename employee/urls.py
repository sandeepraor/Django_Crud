from django.urls import include,path
from . import views
urlpatterns = [
        
    path('',views.homepage),
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:eid>', views.edit),  
    path('update/<int:eid>', views.update),  
    path('delete/<int:eid>', views.destroy),
]