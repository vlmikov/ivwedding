from django.urls import path
from . import views

urlpatterns = [
   
    path('guest/<slug:slug>/', views.home, name="home"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('invitation/<slug:slug>', views.invitation_page, name='invitation_page'),
    path('all_accept/', views.all_accept, name='all_accept' ),

    path('email_test/', views.email_test, name='email_test'),
    path('after_submit/<slug:slug>', views.after_submit, name='after_submit')
    
    
    
]