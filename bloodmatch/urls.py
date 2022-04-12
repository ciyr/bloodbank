from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name= "bloodmatch"
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('register_donor/', views.register_donor, name='register_donor'),
    path('register_receiver',views.register_receiver, name='register_receiver'),
    # path('search_donor/', views.search_donor, name='search_donor'),

]