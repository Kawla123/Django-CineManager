from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('add/', views.movie_create, name='movie_create'),
    path('edit/<int:pk>/', views.movie_update, name='movie_update'),
    path('delete/<int:pk>/', views.movie_delete, name='movie_delete'),
]
