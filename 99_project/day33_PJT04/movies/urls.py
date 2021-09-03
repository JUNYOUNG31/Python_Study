from django.urls import path
from . import views

app_name = 'movies'
# /movies/ + 
urlpatterns = [
     path('new/', views.new, name='new'),
     path('create/', views.create, name='create'),
     path('', views.index, name='index'),
     path('<int:pk>/', views.detail, name='detail'),
     path('<int:pk>/edit/', views.edit, name='edit'),
     path('<int:pk>/update/', views.update, name='update'),
     path('<int:pk>/delete/', views.delete, name='delete'),
]

"""
C
/movies/new/
/movies/create/
R
/movies/
/movies/1/
U
/movies/1/edit/
/movies/1/update/
D
/movies/1/delete

"""