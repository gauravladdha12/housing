from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    listing=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    

    return render(request,'pages/index.html',{'listings':listing})

def about(request):
    realtors=Realtor.objects.order_by('-hire_date')
 
    mvp=Realtor.objects.all().filter(is_mvp=True)
    
    return render(request,'pages/about.html',{
        'realtors':realtors,
        'mvp':mvp
    })
