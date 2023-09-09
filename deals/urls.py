from django.urls import path
from . import views
from .views import *

app_name = 'deals'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:deal_id>/', views.delete_deal, name='delete_deal'),
    path('update/<int:deal_id>/', views.update_deal, name='update_deal'),
]