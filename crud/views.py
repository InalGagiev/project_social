from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import CrudModel
from django.views.generic.base import View
from .forms import *

# домашняя страница
def home(request):
    return render(request, 'crud/home.html')

# представление показа всех статей
class ListRecords(ListView):
    model = CrudModel
    template_name = 'crud/list_records.html'
    context_object_name = 'model'

# детальный просмотр статей
class DetailRecords(DetailView):
    model = CrudModel
    template_name = 'crud/records_detail.html'
    context_object_name = 'model'

# представление создания записей
class CreateRecords(CreateView):
    model = CrudModel
    form_class = ImageForm
    template_name = 'crud/records_form_create.html'
    success_url = '/list_records/'

# представление удаления
class DeleteRecords(DeleteView):
    model = CrudModel
    template_name = 'crud/records_delete.html'
    context_object_name = 'model'
    success_url = '/list_records/'

#это был тест с изображениями
def image_upload_view(request):
    #если данные с формы были отправленны то значит их нужно проверить
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'crud/image-test.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    model = CrudModel
    return render(request, 'crud/image-test.html', {'form': form}, {'model': model})