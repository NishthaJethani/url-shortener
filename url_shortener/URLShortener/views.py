from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import LongtoShort

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello!!!")

def task(request):
    context={"year": "2022", "attendees":["Nishtha", "Adwait"]}
    return render(request, "task.html", context)

def home_page(request):
    print(request.method)
    context={"submitted": False,
            "error":False
    }
    if request.method=="POST":
        print(request.POST)
        data=request.POST
        longurl=data['longurl']
        customname=data['custom_name']
        print(longurl, customname)

        try:

            context['custom_name']=request.build_absolute_uri() + customname
            context['long_url']=longurl
            
    
            obj=LongtoShort(long_url=longurl, custom_name=customname )
            obj.save()
            context['submitted']=True
            context['date']=obj.created_date
            context['clicks']=obj.clicks

        except:
            context['error']=True
    else:
        print("no data entered")
    return render(request, "index.html", context)

def redirect_url(request, customname):
    row=LongtoShort.objects.filter(custom_name=customname)
    if len(row)==0:
        return HttpResponse("Endpoint doesn't exist.")
    obj=row[0]
    long_url=obj.long_url
    obj.clicks+=1
    obj.save()
    return redirect(long_url)

def analytics(request):
    rows=LongtoShort.objects.all()
    context={
        "rows":rows
    }
    return render (request, "analytics.html", context)