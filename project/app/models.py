from itertools import product
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=20)
    viewPassword=models.CharField(max_length=200,null=True)
    
class User(models.Model):
    logid=models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=200)
    Email=models.EmailField()
    Phone=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Image=models.ImageField(upload_to="image")
    
    
class Production_Staff(models.Model):
    logid=models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    image=models.ImageField(upload_to="image")
    
    
class Attendance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateField()
    attendence_status = models.CharField(max_length=200)
    

class Loan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    amount = models.CharField(max_length=200)
    duration_weeks = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200,null=True,blank=True)
    loan_status = models.CharField(max_length=10, default='pending')
    applied_on = models.DateField(auto_now_add=True)
    weekly_payment=models.CharField(max_length=100,null=True)
    
    
class Payment(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE,null=True)
    week_number = models.CharField(max_length=200,null=True)
    amount_paid = models.CharField(max_length=200,null=True)
    paid_on = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    payment_status=models.CharField(max_length=200, default="Pending",null=True)
    
    
class Product(models.Model):
    staff_id = models.ForeignKey(Production_Staff, on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    production_date = models.DateField()
    expiry_date = models.DateField()
    product_stock = models.CharField(max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_img=models.ImageField(upload_to="product")
    pstatus=models.CharField(max_length=100,default="In Stock",null=True)
    
    
class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100,default=1)
    total=models.CharField(max_length=20,null=True)
    booking_date = models.DateField(auto_now_add=True)
    booking_status = models.CharField(max_length=20, default='Booked')
