from winreg import HKEY_LOCAL_MACHINE
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
import datetime
from django.urls import reverse
from .forms import *
# Create your views here.

def home(request):
    return render(request,'main/home.html')

def inputdetails(request):
    if request.method == 'POST':
        form = StudentInputForm(request.POST)
        if form.is_valid():
            obj = Student()
            obj.unique_id = form.cleaned_data['unique_id']
            obj.name = form.cleaned_data['name']
            obj.clas = form.cleaned_data['clas']
            obj.rollno = form.cleaned_data['rollno']
            obj.g1 = form.cleaned_data['g1']
            obj.g2 = form.cleaned_data['g2']
            obj.g3 = form.cleaned_data['g3']
            #finally save the object in db
            obj.save()
            form = StudentInputForm()
            return render(request, 'main/inputdetails.html', {'form': form})
    else:
        form = StudentInputForm()
    return render(request, 'main/inputdetails.html', {'form': form})

def ranklist(request):
    ranklist = Ranklist.objects.all().delete()
    students = Student.objects.all()
    for student in students:
        student.total = student.g1+student.g2+student.g3
        student.save()
    students = Student.objects.all().order_by('-total')
    return render(request,'main/ranklist.html',{'students':students})