from django.urls import path

from . import views

urlpatterns = [
    
    path('hotelsindex/',views.hotelsindex,name='hotelsindex'),
    path('',views.hotelslogin,name='hotelslogin'),
    path('hotelsregister/',views.hotelsregister,name='hotelsregister'),
    path('hotelsotp/',views.hotelsotp,name='hotelsotp'),
    path('hotelsprofile/',views.hotelsprofile,name='hotelsprofile'),
    path('hotelstables/',views.hotelstables,name='hotelstables'),
    path('hotelslogout/',views.hotelslogout,name='hotelslogout'), 
    path('add-hotels/',views.add_hotels,name='add-hotels'), 
    path('hotels_fpassword/',views.hotels_fpassword,name='hotels_fpassword'),
    path('edit/<int:ck>',views.edit,name='edit'),
    path('delete_hotel/<int:pk>',views.delete_hotel,name='delete_hotel'), 

]



