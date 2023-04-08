from django.db import models
import datetime
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    date_on_stubbles_produced=models.DateField()
    price=models.IntegerField(default=0)
    quantity_in_kg=models.FloatField(default=0.0)
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Product.objects.all()

class Category(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Buyer(models.Model):
    aadhar_number=models.CharField(primary_key=True,max_length=12)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    
    
    def register(self):
        self.save()
  
    @staticmethod
    def get_buyer_by_aadhar_number(aadhar_number):
        try:
            return Buyer.objects.get(aadhar_number=aadhar_number)
        except:
            return False

    @staticmethod
    def get_all_farmers():
        return Farmers.objects.all()
  
    def isExists(self):
        if Buyer.objects.filter(aadhar_number=self.aadhar_number):
            return True
  
        return False

    def __str__(self):
        return self.aadhar_number

class Farmer(models.Model):
    aadhar_number=models.CharField(primary_key=True,max_length=12)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    
    #to save data
    def register(self):
        self.save()
  
    @staticmethod
    def get_farmer_by_aadhar_number(aadhar_number):
        try:
            return Farmer.objects.get(aadhar_number=aadhar_number)
        except:
            return False
    
    def isExists(self):
        if Farmer.objects.filter(aadhar_number=self.aadhar_number):
            return True
  
        return False

    def __str__(self):
        return self.aadhar_number

class MonetaryHelp(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    type=models.CharField(max_length=50)
    name=models.CharField(max_length=50)

    def get_help_by_Id(aadhar_number):
        try:
            return MonetaryHelp.objects.get(aadhar_number=aadhar_number)
        except:
            return False
    
    def __str__(self):
        return self.type

class Payment(models.Model):
    payment_id=models.AutoField
    payment_type=models.CharField(max_length=50)
    amount=models.IntegerField(default=0)

    def get_payment_receipt_by_Id(payment_id):
        try:
            return Payment.objects.get(payment_id=payment_id)
        except:
            return False

    def get_all_payment():
        return Payment.objects.all()

    def __str__(self):
        return self.amount





class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.full_name

class AddStuble(models.Model):
    aadhar_number=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    photo=models.CharField(max_length=50)
    weight=models.IntegerField(default=2)
    type=models.CharField(max_length=50)
    amount=models.IntegerField(default=4)
    location=models.CharField(max_length=50)

    def __Str__(self):
        return self.name

class Wallet(models.Model):
    aadhar_number=models.OneToOneField(Farmer,on_delete=models.CASCADE,primary_key=True)
    amount=models.IntegerField(default=0)
    

    def __Str__(self):
        return self.aadhar_number

    def isExists(self):
        if Wallet.objects.filter(id=self.aadhar_number):
            return True
  
        return False

class ToolsRequired(models.Model):
    full_name=models.CharField(max_length=50)
    aadhar=models.IntegerField(max_length=12)
    tools=models.CharField(max_length=50)
    quantity=models.IntegerField(max_length=20)

    def __Str__(self):
        return full_name

class ProvideTools(models.Model):
    full_name=models.CharField(max_length=50)
    aadhar=models.IntegerField(max_length=12)
    tools=models.CharField(max_length=50)
    quantity=models.IntegerField(max_length=20)

    def __Str__(self):
        return full_name

class PaymentDetails(models.Model):
    Card_holder=models.CharField(max_length=50)
    Card_Number=models.CharField(max_length=16)
    expiry_data=models.CharField(max_length=5)
    CVC=models.CharField(max_length=3)

    def __Str__(self):
        return Card_holder

class Order(models.Model):
    product = models.ForeignKey(AddStuble,
                                on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')