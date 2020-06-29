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


class security_check(models.Model):
    userid=models.CharField(max_length=100)
    secu_ques1=models.CharField(max_length=100)
    secu_ques2 = models.CharField(max_length=100)
    secu_ques3 = models.CharField(max_length=100)
    secu_ques4 = models.CharField(max_length=100)

    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)

class complaints(models.Model):
    complaint_id=models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    card_no = models.CharField(max_length=100)
    transaction_id= models.CharField(max_length=100)


class bank_details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Account_balance(models.Model):
    user_id = models.CharField(max_length=100)
    cus_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    acct_num = models.CharField(max_length=100)

    bank = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)














