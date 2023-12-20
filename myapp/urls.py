from django.urls import path

from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/',views.login,name = 'login'),
    path('home/',views.home,name = 'home'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect'),
    path('logout/',views.logout,name = 'logout'),
]