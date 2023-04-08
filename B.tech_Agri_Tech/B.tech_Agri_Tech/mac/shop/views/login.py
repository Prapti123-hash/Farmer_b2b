from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from shop.models import Buyer
from shop.models import Farmer
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        aadhar_number = request.POST.get ('aadhar_number')
        password = request.POST.get ('password')
        category= request.POST.get('category')

        if category == "buyer" :
            buyer = Buyer.get_buyer_by_aadhar_number (aadhar_number)
            error_message = None
            if buyer:
                flag = check_password (password, buyer.password)
                if flag:
                    request.session['buyer'] = buyer.aadhar_number

                    if Login.return_url:
                        return HttpResponseRedirect (Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect ('buyer')
                else:
                    error_message = 'Invalid !!'
            else:
                error_message = 'Invalid !!'

            print (aadhar_number, password)
            return render (request, 'login.html', {'error': error_message})
        
        else:
            farmer = Farmer.get_farmer_by_aadhar_number (aadhar_number)
            error_message = None
            if farmer:
                flag = check_password (password, farmer.password)
                if flag:
                    request.session['farmer'] = farmer.aadhar_number

                    if Login.return_url:
                        return HttpResponseRedirect (Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect ('farmer',aadhar_number)
                else:
                    error_message = 'Invalid !!'
            else:
                error_message = 'Invalid !!'

            print (aadhar_number, password)
            return render (request, 'login.html', {'error': error_message})
            

def logout(request):
    request.session.clear()
    return redirect('Home')
