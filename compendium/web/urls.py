from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('weapon/<int:weapon_id>/', views.weapon_detail, name='weapon'),
    path('armor/<int:armor_id>/', views.armor_detail, name='armor'),
    path('class/<int:char_class_id>/', views.class_detail, name='class'),
    path('race/<int:char_race_id>/', views.race_detail, name='race'),
    path('weapons/', views.weapons, name='weapons'),
    path('armors/', views.armors, name='armors'),
    path('classes/', views.classes, name='classes'),
    path('races/', views.races, name='races'),
    path('additem/', views.additem, name='additem'),
    path('newsearch/', views.newsearch, name='newsearch'),
]