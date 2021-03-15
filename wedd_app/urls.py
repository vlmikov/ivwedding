from django.urls import path
from . import views

urlpatterns = [
   
    path('guest/<slug:slug>/', views.home, name="home"),
    path('dashboard/', views.dashboard, name='dashboard')
    #path('test/', views.invitation, name = "invitation")
    
    
]