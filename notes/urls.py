from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/',views.updateTask, name="update_task"),
    path('delete_task/<str:pk>',views.deleteTask, name="delete_task")
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('loggedout/', views.loggedout, name='loggedout'),
    # path('settings/', views.settings, name='settings'),
    # path('home/', views.home, name='home')
]
