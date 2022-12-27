from django.urls import include,path
from . import views
urlpatterns = [
        
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('login/',views.login_view),
    path('',views.index),
    path('reg/',views.register_request)
]