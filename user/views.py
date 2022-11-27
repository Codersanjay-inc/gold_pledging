from django.shortcuts import render,redirect
from .models import Destination


# Create your views here.
def home(request):
    return render(request,"home.html")


def result(request):
    s=Destination.objects.all()
    return render(request,"result.html",{"s":s})


def add(request):
    print("hello submmited")
    if request.method=='POST':

        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        ammount = request.POST["ammount"]
        address = request.POST["address"]

        data_store = Destination(name=name,email=email,mobile=mobile,ammount=ammount,address=address)

        data_store.save()

        return redirect('final')
def final(request):
    return render(request,"final.html")        
   
