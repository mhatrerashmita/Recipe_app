from django.contrib import admin
from django.urls import path
from foodapp import views
from django.views.i18n import set_language

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('contact/', views.contact,name='contact'),
    path('register/', views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('add_recipe/', views.add_recipe_view, name='add_recipe'),
    path('i18n/', set_language, name='set_language'),
    # path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),
]
