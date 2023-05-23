from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    #return HttpResponse("This is Homepage")
    context = {
        'variable1':"Abhishek",
        'variable2':"Ashu"
    }
    return render(request,"index.html")
def about(request):
    #return HttpResponse("This is Aboutpage")
     return render(request,"about.html")
def services(request):
    #return HttpResponse("This is Servicespage")
     return render(request,"services.html")
def servsoft(request):
    #return HttpResponse("This is Servicespage")
     return render(request,"servsoft.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Detaiks has been sent. Thanks')
    #return HttpResponse("This is Contactpage")
    return render(request,"contact.html")

