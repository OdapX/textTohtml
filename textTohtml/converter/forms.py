from django.forms import ModelForm
from converter.models import Text
from ckeditor.widgets import CKEditorWidget
from django import forms

class TextForm(forms.ModelForm):
        body = forms.CharField(widget=CKEditorWidget(),label="Text Editor",required=False)
        class Meta:
            model = Text
            fields = '__all__'

