from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import *
# Create your views here.

from .models import Listing

def index(request):

    listing=Listing.objects.order_by('-list_date').filter(is_published=True)

    #pagination
    paginator= Paginator(listing,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    return render(request,'listings/listings.html',{'listings':paged_listings})

def listing(request,listing_id):

    listing=get_object_or_404(Listing,pk=listing_id)
    return render(request,'listings/listing.html',{
        'listing':listing
    })

def search(request):

    queryset_list= Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET :
        keywords=request.GET['keywords']
        if keywords :
            queryset_list=queryset_list.filter(description__icontains=keywords)
    
    #city
    if 'city' in request.GET :
        city=request.GET['city']
        if city :
            queryset_list=queryset_list.filter(city__iexact=city)

    #state
    if 'bedrooms' in request.GET :
        bedrooms=request.GET['bedrooms']
        if bedrooms :
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)

    #bedrooms
    if 'city' in request.GET :
        city=request.GET['city']
        if city :
            queryset_list=queryset_list.filter(city__iexact=city)

    #price
    if 'price' in request.GET :
        price=request.GET['price']
        if price :
            queryset_list=queryset_list.filter(price__iexact=price)

    return render(request,'listings/search.html',{
        'listings':queryset_list,
        'values':request.GET
    })
