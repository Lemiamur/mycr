from django.urls import path
from . import views
from .views import *

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('update/<int:contact_id>/', views.update_contact, name='update_contact'),
    path('contacts/delete_selected/', views.delete_selected_contacts, name='delete_selected_contacts'),
]