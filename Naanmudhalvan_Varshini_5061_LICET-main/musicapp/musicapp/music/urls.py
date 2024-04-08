from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('upload/', views.upload_song, name='upload_song'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
]
