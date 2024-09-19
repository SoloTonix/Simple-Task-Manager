from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:pk>/', update_task, name='update-task'),
    path('complete-task/<int:pk>/', complete_task, name='complete-task'),
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),
]