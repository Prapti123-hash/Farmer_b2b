from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from shop.models import Buyer
from django.views import View
from shop.models import Farmer
from shop.models import AddStuble
from shop.models import ToolsRequired
from shop.forms import AddStubleform
from django.contrib import messages
from shop.models import Wallet
class Farmers (View):
    def get(self, request,id):
        farmer=Farmer.objects.get(pk=id)
        return render (request, 'farmer.html',{'farmer':farmer})

def addStuble(request,id):
    farmer=Farmer.objects.get(pk=id)
    if request.method=="POST":
        name=request.POST['name']
        photo=request.POST['photo']
        weight=request.POST['weight']
        type=request.POST['type']
        amount=request.POST['amount']
        location=request.POST['location']
        
        stubbles=AddStuble.objects.create(name=name,weight=weight,type=type,amount=amount,location=location,aadhar_number=farmer)
        messages.success(request,'Data has been submitted')
    return render(request,'addStuble.html',{'farmer':farmer})

def stubbles_formadd(request):
    if request.method=="POST":
        name=request.POST['name']
        photo=request.POST['photo']
        weight=request.POST['weight']
        type=request.POST['type']
        amount=request.POST['amount']
        location=request.POST['location']
        stubbles=AddStuble(name=name,weight=weight,type=type,amount=amount,location=location)
        stubbles.save()
    return render(request,'addStuble.html')

def stubbles_form(request,id):
    stubble_list=AddStuble.objects.get(id=id)
    form=AddStubleform(request.POST,instance=stubble_list)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully")
    return render(request,'updateStuble.html',{"AddStuble":stubble_list})



def viewStuble(request,id):
        stuble_list=AddStuble.objects.filter(aadhar_number=id)
        return render(request,'viewStuble.html',{'stuble_list':stuble_list})

def toolsRequired(request,id):
        farmer=Farmer.objects.get(pk=id)
        if request.method=="POST":
            
            tools=request.POST['tools']
            quantity=request.POST['quantity']
            tools_p=ToolsRequired.objects.create(full_name=farmer.name,aadhar=farmer.aadhar_number,tools=tools,quantity=quantity)
            messages.success(request,'Data has been submitted')
        return render(request,'toolsRequired.html',{'farmer':farmer})

def tools_form(request,id):
        if request.method=="POST":
            full_name=request.POST['full_name']
            aadhar=request.POST['aadhar']
            tools=request.POST['tools']
            quantity=request.POST['quantity']
            tools_p=ToolsRequired(full_name=full_name,aadhar=aadhar,tools=tools,quantity=quantity)
            tools_p.save()
        return render(request,'toolsRequired.html',{'farmer':farmer})

def updateStubble(request,id):
    stuble_list=AddStuble.objects.get(id=id)
    farmer=Farmer.objects.get(pk=stuble_list.aadhar_number)
    if request.method=="POST":
        name=request.POST['name']
        photo=request.POST['photo']
        weight=request.POST['weight']
        type=request.POST['type']
        amount=request.POST['amount']
        location=request.POST['location']
        stubbles=AddStuble(id=id,name=name,weight=weight,type=type,amount=amount,location=location,aadhar_number=farmer)
        stubbles.save()
    return render(request,'updateStuble.html',{"AddStuble":stuble_list})

def updateAddStuble(request,id):
    stubble_list=AddStuble.objects.get(id=id)
    form=AddStubleform(request.POST,instance=stubble_list)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully")
    return render(request,'updateStuble.html',{"AddStuble":stuble_list})

def deleteStuble(request,id):
    delrec=AddStuble.objects.get(id=id)
    delrec.delete()
    stuble_list=AddStuble.objects.all()
    return render(request,'viewStuble.html',{'stuble_list':stuble_list})

def wallet(request,id):
    
    farmer=Farmer.objects.get(pk=id)
    try:
        wallet = Wallet.objects.get(aadhar_number=farmer.aadhar_number)
        
    except Wallet.DoesNotExist:
        wallet = Wallet.objects.create(amount=0,aadhar_number=farmer)
    
    return render(request,'wallet.html',{'wallet':wallet})

def contactfarmer(request,id):
    farmer=Farmer.objects.get(pk=id)
    if request.method=='POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact.objects.create(full_name=full_name,email=email,message=message)
        messages.success(request,'Data has been submitted')
    return render(request,'contactfarmer.html',{'farmer':farmer})

def contact_formfarmer(request,id):
    farmer=Farmer.objects.get(pk=id)
    if request.method=="POST":
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact(full_name=full_name,email=email,message=message)
        contact.save()
        
    return render(request,'contactfarmer.html',{'farmer':farmer})





