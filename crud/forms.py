from django import forms
from .models import CrudModel
from tinymce.widgets import TinyMCE


class ImageForm(forms.ModelForm):
    class Meta:
        model = CrudModel
        fields = ('title', 'full_text')
        widgets = {
            "full_text": TinyMCE(mce_attrs={'cols': 80, 'rows': 30})
        }
