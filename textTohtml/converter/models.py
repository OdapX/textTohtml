from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Text(models.Model) :
       
       body = RichTextField(blank=True,null=True)