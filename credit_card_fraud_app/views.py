from django.shortcuts import render
from .models import bank_details
from .models import customer_details
from .models import account_details
from .models import Account_balance
from django.contrib.sessions.models import Session
import string
import random
# Create your views here.
def index(request):
    return render(request,'index.html')
def banklogin(request):
    return render(request,'banklogin.html')
def customerlogin(request):
    return render(request,'customerlogin.html')
def analyserlogin(request):
    return render(request,'analyserlogin.html')
def bankhome(request):
    return render(request,'bankhome.html')
def add_customer_details(request):
    return render(request,'add_customer_details.html')
def add_account_details(request):
    return render(request,'add_account_details.html')
def customerhome(request):
    return render(request,'customerhome.html')
def analyserhome(request):
    return render(request,'analyserhome.html')

def bank_sign(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = bank_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['bankname'] = x.username
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return render(request, 'bankhome.html', {'bankname': x.username})
    return render(request, 'banklogin.html', {'msg': "Incorrect username or password.Try again"})

def bank_logout(request):
    # logout(request)
    # return render(request, 'home.html')

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['bankname'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'banklogin.html')

def customer_sign(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = customer_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['cusname'] = x.username
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return render(request, 'customerhome.html', {'cusname': x.username})
    return render(request, 'customerlogin.html', {'msg': "Incorrect username or password.Try again"})


def customer_logout(request):
    # logout(request)
    # return render(request, 'home.html')

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['cusname'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'customerlogin.html')

def customer_profiles(request):
    db = customer_details(customer_name = request.POST.get('cname'),
                        email=request.POST.get('email'), phone=request.POST.get('phone'),
                        house_number=request.POST.get('hname'), street=request.POST.get('street'),
                        place=request.POST.get('place'), district=request.POST.get('district'),
                        state=request.POST.get('state'), pincode=request.POST.get('pin'),


                        username=request.POST.get('uname'), password=request.POST.get('password'))

    db.save()
    return render(request, 'add_customer_details.html', {'msg': "Successfully Inserted"})


def view_customer_details(request):
    customer = customer_details.objects.all()
    return render(request, 'view_customer.html', {'customer': customer})


def customer_account(request):
    n = 11
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=n))
    c = 16
    c1 = '' .join(random.choices(string.digits, k=c))
    a = 16
    a1 = '' .join(random.choices(string.digits, k=a))

    p = 4
    p1 = '' .join(random.choices(string.digits, k=p))



    db = account_details(acct_num = a1,
                        branch=request.POST.get('bname'), card_num=c1,
                        customer_id=request.POST.get('cid'), customer_name=request.POST.get('cname'),
                        date=request.POST.get('date'), email=request.POST.get('email'),
                        ifsc=res, phone=request.POST.get('phone'),


                        pin=p1, place=request.POST.get('place'),bank_name=request.POST.get('bankname'))

    db.save()
    return render(request, 'add_account_details.html', {'msg': "Successfully Inserted"})

def view_account_details(request):
    account = account_details.objects.all()
    return render(request, 'view_account.html', {'account': account})

def cus_profile(request):
    cusname = request.session['cusname']
    customer = customer_details.objects.get(username=cusname)
    return render(request, 'cus_profile.html', {'customer': customer,'cusname':cusname})

def update_pro(request):

        cname = request.session['cusname']


        obj = customer_details.objects.get(username=cname)

        obj.customer_name = request.POST.get('cname')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.username = request.POST.get('uname')
        obj.password = request.POST.get('password')
        obj.save()

        customer = customer_details.objects.get(username=cname)

        return render(request, 'cus_profile.html', {'msg': 'Successfully Updated','customer': customer,'cusname':cname})


def acct_details(request):
    cusname = request.session['cusname']
    details = customer_details.objects.get(username=cusname)
    c_id = details.id
    #print(c_id)
    acct = account_details.objects.get(customer_id = c_id)
    return render(request, 'acct_details.html', {'acct': acct,'cusname':cusname})

def add_payment(request):
    cusname = request.session['cusname']
    details = customer_details.objects.get(username=cusname)
    c_id = details.id
    #print(c_id)
    return render(request,'add_payment.html',{'cusname':cusname,'c_id':c_id})


def save_payment(request):
    cusname = request.session['cusname']
    db = Account_balance(user_id=request.POST.get('c_id'),cus_name = request.POST.get('cname'),
                        email=request.POST.get('email'), phone=request.POST.get('phone'),
                        acct_num=request.POST.get('accnt'), bank=request.POST.get('bank'),
                        branch=request.POST.get('branch'), date=request.POST.get('date'),
                        amount=request.POST.get('amount'))

    db.save()
    return render(request, 'add_payment.html', {'msg': "Successfully Inserted",'cusname':cusname})



def view_balance(request):
    cusname = request.session['cusname']
    details = customer_details.objects.get(username=cusname)
    c_id = details.id
    #print(c_id)
    balance = Account_balance.objects.get(user_id = c_id)
    return render(request, 'view_balance.html', {'balance': balance,'cusname':cusname})

def make_transaction(request):
    cusname = request.session['cusname']
    return render(request, 'make_transaction.html', {'cusname': cusname})