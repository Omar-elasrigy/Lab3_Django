from django.urls import path
from .views import *

urlpatterns = [
    path('',list,name='list'),
    path('Update/',update,name='update'),
    path('Delete/',delete,name='delete'),
    path('Create/',create,name='create'),
    path('show_details/',show_details,name='show_details'),
]
