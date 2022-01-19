from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'), 
    path('about/', views.about,name='about'),
    path('profile/', views.profile,name='profile'),  
    path('hotels2/', views.hotels2,name='hotels2'),
    path('register/', views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('fpassword/',views.fpassword,name='fpassword'),
    path('booking/',views.booking,name='booking'),
    path('Aview_hotels/<int:pk>',views.Aview_hotels,name='Aview_hotels'),
]



