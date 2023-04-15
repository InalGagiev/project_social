from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class CrudModel(models.Model):
    title = models.CharField(max_length=50)
    full_text = tinymce_models.HTMLField('полный текст', null=True)
    date = models.DateTimeField(null=True)
    # upload_to равносилен media/images
    image = models.ImageField(upload_to='images', null=True)
    # тут мы используем тип связи ForeignKey
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'list/get/{self.title}'

    class Meta:
        ordering = ['title']

