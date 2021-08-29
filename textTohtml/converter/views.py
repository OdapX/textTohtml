from django.shortcuts import render
from converter.forms import TextForm

def Converter(request):
           form = TextForm(request.POST)
         
           return render(request,'converter/main.html',{'form':form})
