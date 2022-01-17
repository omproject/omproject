from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'), 
    path('about/', views.about,name='about'),
    path('profile/', views.profile,name='profile'), 
    path('view-hotel/', views.view_hotel,name='view-hotel'), 
    path('services/', views.services,name='services'),
    path('register/', views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('fpassword/',views.fpassword,name='fpassword'),
]



