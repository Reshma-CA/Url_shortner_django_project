from django.urls import path

from . import views
urlpatterns = [
    path('', views.adminlogin, name='adminlogin'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('admin_logout/',views.admin_logout,name = 'admin_logout')
   

]