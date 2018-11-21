# index的views.py
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def mydate(request, year, month, day):
    return HttpResponse(str(year) +'/'+ str(month) +'/'+ str(day))
