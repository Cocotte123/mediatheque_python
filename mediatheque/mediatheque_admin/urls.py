from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_emprunteur/<int:id>/', views.delete_emprunteur, name='delete_emprunteur'),
    path('update_emprunteur/<int:id>/', views.update_emprunteur, name='update_emprunteur'),
]
