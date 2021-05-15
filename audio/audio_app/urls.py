from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create, name='create'),
    path('delete/<audioFileType>/<int:id>', delete, name='delete'),
    path('update/<audioFileType>/<int:id>', update, name='update'),
    path('listdetail/<audioFileType>', listdetail, name='list'),
    path('listdetail/<audioFileType>/<int:id>', listdetail, name='detail'),
]