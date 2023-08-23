from django.urls import path
from . import views

app_name = 'departments'  # This should match the name of your app

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    # Add more URL patterns for other views
    path('blank/', views.blank_page, name='blank'),
    path('maps/', views.google_maps, name='maps'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('forms/', views.forms, name='forms'),
    path('typography/', views.typography, name='typography'),
    path('upgrade/', views.upgrade_to_pro, name='upgrade'),
]
