from django.urls import include,path
from . import views
urlpatterns = [
        
    path('',views.homepage),
    path('admin-dashboard', views.admindashboard),
    path('employee-dashboard',views.employeedashboard),
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:eid>', views.edit),  
    path('update/<int:eid>', views.update),  
    path('delete/<int:eid>', views.destroy),
    path('verify_employee/<int:id>',views.verify_employee)
]