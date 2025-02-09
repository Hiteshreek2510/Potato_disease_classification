from django.shortcuts import render
from .form import Imageform
from .models import Image
from django import forms
# Create your views here.
def index(request):
    if request.method=='POST':
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,'index.html',{'obj':obj})
    else:
        form=Imageform()
    img=Image.objects.all()
    return render(request,'index.html',{'img':img,'form':form})
