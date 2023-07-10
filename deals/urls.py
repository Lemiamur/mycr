from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task_status/', views.update_task_status, name='update_task_status'),
]