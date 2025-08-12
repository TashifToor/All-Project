from django.shortcuts import render
from datetime import datetime
from django.contrib import messages

from gymm.models import contact
def index(request):
     return render(request,"index.html")
def ContactUs(request):        
        if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          desc=request.POST.get('desc')
          Contact=contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
          Contact.save()
          messages.success(request, "You Messege has Been sent!")
        return render(request,"Contact Us.html")
   
   


def home(request):
     return render(request,'home.html')
def AboutUs(request):
     return render(request,'About Us.html')
def JoinUs(request):
     return render(request,'Join Us.html')

def Pricing(request):
     return render(request,'Pricing.html')
def PersonalTrainer(request):
     return render(request,'Personal Trainer.html')
def CorporatePlans(request):
     return render(request,'Corporate Plans.html')
def Membership(request):
     return render(request,'Membership.html')
def Classes(request):
     return render(request,'Classes.html')
def Trainers(request):
     return render(request,'Trainers.html')
def Gallery(request):
     return render(request,'Gallery.html')


def SpecialOffers(request):
     return render(request,'Special Offers.html')

