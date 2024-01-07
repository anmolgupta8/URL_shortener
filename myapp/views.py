from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def home_page(request):
    return render(request,'index.html')

def task_page(request):
    details = {
        'name':'Anmol Gupta',
        'age':21,
        'company':'O(1) Coding Club',
        'role':'Python Backend Developer'
    }
    return render(request,'task.html',{'data':details})