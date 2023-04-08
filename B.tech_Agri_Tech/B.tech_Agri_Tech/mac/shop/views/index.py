from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from shop.models import Buyer
from shop.models import Farmer
from django.views import View
from shop.models import Contact
from shop.models import AddStuble
class Index(View):
    def get(self,request):
        return render(request,'index.html')

def contact(request):
    
    if request.method=='POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact.objects.create(full_name=full_name,email=email,message=message)
        messages.success(request,'Data has been submitted')
    return render(request,'contact.html')

def contact_form(request):
    
    if request.method=="POST":
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact(full_name=full_name,email=email,message=message)
        contact.save()
        
    return render(request,'contact.html')

def stuble(request):
        stuble_list=AddStuble.objects.all()
        return render(request,'stuble.html',{'stuble_list':stuble_list})
