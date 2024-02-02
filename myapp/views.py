from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LongToShort

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def home_page(request):
    # print(request.method)
    context = {
        'submitted' : False,
        'error' : False
    }
    if(request.method == 'POST'):
        # print(request.POST)
        data = request.POST; # data is a dictionary
        long_url = data['longurl']
        custom_name = data['custom_name']
        print(long_url)
        print(custom_name)
        try:    
            obj = LongToShort(
                long_url = long_url,
                short_url = custom_name
            )
            obj.save()
            date = obj.date
            clicks = obj.clicks
            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
            context["date"] = date
            context["clicks"] = clicks
            context['submitted'] = True
        except:
            context["error"] = True
    else:
        print("User not sending anything")

    return render(request,'index.html',context)

def redirect_url(request,short_url):
    # print(shorturl)
    row = LongToShort.objects.filter(short_url = short_url)
    if(len(row) == 0):
        return HttpResponse("There is no such row")
    obj = row[0]
    long_url = obj.long_url
    obj.clicks = obj.clicks+1
    obj.save()
    # print(row)
    return redirect(long_url)

def all_analytics(request):
    rows = LongToShort.objects.all()
    context = {
        "rows":rows
    }
    return render(request,'all-analytics.html',context)

def task_page(request):
    details = {
        'name':'Anmol Gupta',
        'age':21,
        'company':'O(1) Coding Club',
        'role':'Python Backend Developer'
    }
    return render(request,'task.html',{'data':details})