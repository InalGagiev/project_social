from django.urls import path, include
from .views import *

urlpatterns = [
    #домашняя страница
    path('', home, name='home'),
    #страница просмотра всех записей
    path('list_records/', ListRecords.as_view(), name='list_records'),
    #страница детального просмотра статей
    path('list_records/detail/<int:pk>/', DetailRecords.as_view(), name='list_detail'),
    #страница добавления статей
    path('list_records/create', CreateRecords.as_view(), name='list-create'),
    #страница удаления статьи
    path('list_records/detail/<int:pk>/delete', DeleteRecords.as_view(), name='list-delete'),
    #страница загрузки изображений
    path('image-test/', image_upload_view, name='image'),
]

