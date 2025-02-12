from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),  # List of available equipment
    path('borrow/<int:equipment_id>/', views.borrow_equipment, name='borrow_equipment'),  # Borrow equipment
    path('return/<int:borrow_id>/', views.return_equipment, name='return_equipment'),  # Return equipment
]
