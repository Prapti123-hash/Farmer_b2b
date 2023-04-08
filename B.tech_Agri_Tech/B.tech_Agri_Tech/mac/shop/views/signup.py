from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models import Buyer
from shop.models import Farmer
from django.views import View
from django.contrib import messages

class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        name=postData.get('name')
        print(name)
        aadhar_number = postData.get ('aadhar_number')
        location= postData.get ('location')
        category= postData.get('category')
        password = postData.get ('password')
        confirm_password=postData.get('confirm_password')
        # validation
        value = {
            'aadhar_number': aadhar_number,
            'location': location,
            'category': category,
            'name':name,
        }
        error_message = None

        #Assigning user category wise
        if category == "buyer" :
            buyer = Buyer (aadhar_number=aadhar_number,
                             name=name,
                             password=password,
                             confirm_password=confirm_password,
                             location=location,
                             )
            error_message = self.validateBuyer (buyer)

        
            if not error_message:
                print (name,aadhar_number, password, location)
                buyer.password = make_password (buyer.password)
                buyer.register ()
                messages.success(request,'Account created successfully. To login to your account kindly scroll down the page.')
                return redirect ('signup')
            else:
                data = {
                    'error': error_message,
                
                    'values': value
                }
        else:
            farmer = Farmer (aadhar_number=aadhar_number,
                             name=name,
                             password=password,
                             confirm_password=confirm_password,
                             location=location,
                             )
            error_message = self.validateFarmer (farmer)

        
            if not error_message:
                print (name,aadhar_number, password, location)
                farmer.password = make_password (farmer.password)
                farmer.register ()
                messages.success(request,'Account created successfully. To login to your account kindly scroll down the page.')
                return redirect ('signup')
            else:
                data = {
                    'error': error_message,
                
                    'values': value
                }

        return render (request, 'signup.html', data)

    def validateBuyer(self, buyer):
        error_message = None
        if (not buyer.name):
            error_message = "Please Enter your  Name !!"
        elif len (buyer.name) < 3:
            error_message = ' Name must be 3 char long or more'
        elif not buyer.aadhar_number:
            error_message = 'Please Enter your adhar number'
        elif len (buyer.aadhar_number) != 12:
            error_message = 'Aadhar number must be 12 character long'
        elif not buyer.location:
            error_message = 'Enter your location'
        
        elif len (buyer.password) < 5:
            error_message = 'Password must be 5 char long'
        
        elif buyer.isExists ():
            error_message = 'Adhar number  Already Registered..'
        # saving


        return error_message

    def validateFarmer(self, farmer):
        error_message = None
        if (not farmer.name):
            error_message = "Please Enter your  Name !!"
        elif len (farmer.name) < 3:
            error_message = ' Name must be 3 char long or more'
        elif not farmer.aadhar_number:
            error_message = 'Please Enter your adhar number'
        elif len (farmer.aadhar_number) != 12:
            error_message = 'Aadhar number must be 12 character long'
        elif not farmer.location:
            error_message = 'Enter your location'
        
        elif len (farmer.password) < 5:
            error_message = 'Password must be 5 char long'
        
        elif farmer.isExists ():
            error_message = 'Adhar number  Already Registered..'
        # saving


        return error_message

def accountSuccess(request):
    return render (request, 'accountSuccess.html')