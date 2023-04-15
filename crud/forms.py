from django import forms
from .models import *
from tinymce.widgets import TinyMCE


class ImageForm(forms.ModelForm):
    class Meta:
        model = CrudModel
        fields = ('title', 'full_text', 'category')
        widgets = {
            "full_text": TinyMCE(mce_attrs={'cols': 80, 'rows': 30})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']