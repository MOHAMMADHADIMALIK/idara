from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login
import random
# Create your views here.
from .models import dropdownoptions,donation
def login(request):
    global user_auth_check
    user_auth_check = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth_check = authenticate(request,username=username,password=password)
        if user_auth_check == None:
               return redirect("/")
        else:
            user_login(request,user_auth_check)
            print("user login hova")
            return redirect('main/')
    return render(request,'index.html')

def main(request):
    #  if user_auth_check == None:
    #       return redirect('/')
     data = {"data":list(dropdownoptions.objects.all().values())}
     return render(request,"main.html",data)


def savedata(request):
     if request.method == 'POST':
        randomn = random.randint(1000000000,9999999999)
        cord = request.POST['cord']
        account = request.POST['account']
        onoff = request.POST['onoff']
        ldhead = request.POST['ldhead']
        amount = request.POST['amount']
        donations = donation()
        donations.crorde = cord
        donations.amount = amount
        donations.ledgerhead = ldhead
        donations.onoroff = onoff
        donations.accounttype = account
        donations.transitionid = randomn
        donations.save()
        return redirect("main")
     return redirect('login')