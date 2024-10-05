from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.register, name="signup"), 
    path('success/<str:username>/', views.success, name="success"), 
]
