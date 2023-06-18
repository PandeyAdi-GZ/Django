from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('', views.display, name='display'),
]
