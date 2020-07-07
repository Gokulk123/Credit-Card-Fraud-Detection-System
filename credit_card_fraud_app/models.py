from django.db import models

# Create your models here.

class customer_details(models.Model):
    customer_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone = models.CharField(max_length=100)
    house_number=models.CharField(max_length=100)
    street = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class account_details(models.Model):
    customer_name=models.CharField(max_length=100,default='SOME STRING')
    email=models.CharField(max_length=100,default='SOME STRING')
    phone=models.CharField(max_length=100,default='SOME STRING')
    place=models.CharField(max_length=100,default='SOME STRING')
    pin=models.CharField(max_length=100,default='SOME STRING')
    date=models.CharField(max_length=100,default='SOME STRING')
    acct_num = models.CharField(max_length=100,default='SOME STRING')
    branch = models.CharField(max_length=100,default='SOME STRING')
    bank_name = models.CharField(max_length=100, default='SOME STRING')
    ifsc = models.CharField(max_length=100,default='SOME STRING')
    card_num = models.CharField(max_length=100,default='SOME STRING')
    customer_id = models.CharField(max_length=100,default='SOME STRING')
    f_place = models.CharField(max_length=100,default='SOME STRING')
    f_pet = models.CharField(max_length=100,default='SOME STRING')
    f_food = models.CharField(max_length=100,default='SOME STRING')

class transaction_details(models.Model):
    cus_name = models.CharField(max_length=100,default='SOME STRING')
    email=models.CharField(max_length=100,default='SOME STRING')
    phone = models.CharField(max_length=100,default='SOME STRING')
    acct_num = models.CharField(max_length=100, default='SOME STRING')
    bank_name = models.CharField(max_length=100, default='SOME STRING')
    branch = models.CharField(max_length=100, default='SOME STRING')
    date = models.DateField()
    customer_id = models.CharField(max_length=100, default='SOME STRING')
    amount = models.CharField(max_length=20)
    result = models.CharField(max_length=100, default='SOME STRING')




class bank_details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

















