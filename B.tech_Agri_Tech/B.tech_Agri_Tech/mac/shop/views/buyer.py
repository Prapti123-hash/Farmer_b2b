from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from shop.models import Buyer
from django.views import View
from shop.models import Farmer
from shop.models import AddStuble
from shop.models import ToolsRequired
from shop.models import ProvideTools
from shop.models import PaymentDetails
from shop.models import Wallet
from django.contrib import messages
class Buyer (View):
    def get(self, request):
        return render (request, 'buyer.html')

def provideTools(request):
    if request.method=="POST":
        full_name=request.POST['full_name']
        aadhar=request.POST['aadhar']
        tools=request.POST['tools']
        quantity=request.POST['quantity']
        p_tools=ProvideTools.objects.create(full_name=full_name,aadhar=aadhar,tools=tools,quantity=quantity)
        messages.success(request,'Data has been submitted')
    return render(request,'provideTools.html')

def provide_tools(request):
    if request.method=="POST":
        full_name=request.POST['full_name']
        aadhar=request.POST['aadhar']
        tools=request.POST['tools']
        quantity=request.POST['quantity']
        p_tools=ProvideTools(full_name=full_name,aadhar=aadhar,tools=tools,quantity=quantity)
        p_tools.save()
        messages.success(request,'Data has been submitted')
    return render(request,'provideTools.html')

def buyerView(request):
    stuble_list=AddStuble.objects.all()
    return render(request,'buyerView.html',{'stuble_list':stuble_list})

def payment(request):
    if request.method=="POST":
        Card_holder=request.POST['Card_holder']
        Card_Number=request.POST['Card_Number']
        expiry_data=request.POST['expiry_data']
        CVC=request.POST['CVC']
        payment_table=PaymentDetails.objects.create(Card_holder=Card_holder,Card_Number=Card_Number,expiry_data=expiry_data,CVC=CVC)
        messages.success(request,'Data has been submitted')
    return render(request,'payment.html')

def payment_done(request):
    if request.method=="POST":
        Card_holder=request.POST['Card_holder']
        Card_Number=request.POST['Card_Number']
        expiry_data=request.POST['expiry_data']
        CVC=request.POST['CVC']
        payment_table=PaymentDetails(Card_holder=Card_holder,Card_Number=Card_Number,expiry_data=expiry_data,CVC=CVC)
        payment_table.save()
        
    return render(request,'paymentdone.html')



def buyNow(request,id):
    stubble=AddStuble.objects.get(pk=id)
    farmer=Farmer.objects.get(pk=stubble.aadhar_number)
    amount=stubble.amount
    aadhar_number=stubble.aadhar_number
    try:
        wallet = Wallet.objects.get(aadhar_number=farmer.aadhar_number)
        wallet.amount=wallet.amount+amount
        walletn=Wallet(aadhar_number=stubble.aadhar_number,amount=wallet.amount)
        walletn.save()
    except Wallet.DoesNotExist:
        wallet = Wallet.objects.create(amount=amount,aadhar_number=farmer)
    delrec=AddStuble.objects.get(id=id)
    delrec.delete()
    stuble_list=AddStuble.objects.all()
    return render(request,'payment.html')

def home(request):
    return redirect('buyer')

    
    