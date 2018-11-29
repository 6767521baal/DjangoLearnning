# index的views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import csv
# Create your views here.
def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    return render(request, 'index.html',context=locals(), status=200)

def mydate(request, year, month, day):
    return HttpResponse(str(year) +'/'+ str(month) +'/'+ str(day))

def myyear(request, year):
    return render(request, 'myyear.html')

def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month':month})

def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="firstDownloadFile.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response