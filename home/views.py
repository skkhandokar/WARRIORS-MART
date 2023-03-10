from django.shortcuts import render
from items.models import Product
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages
from home.models import Contact_us

from .utils import paginationProject

# Create your views here.


def home(request):
    product = Product.objects.all()
    custom_range, products = paginationProject(request, product, 2)
    return render(request, 'index.html', context={'products': products, 'custom_range': custom_range})


def contactPage(request):
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= name
        message= request.POST.get('message')
        admin='warriors.mart.contact@gmail.com'
        
        if subject and message and email:
           contact=Contact_us(sender_name=name,from_email=email,subject=subject,message=message)
           contact.save()
           send_mail(subject,message,email, [admin,email,name])
           messages.success(request,'Succesfully Send Message!')
        
         
        else:
           messages.error(request,'Make sure all fields are entered and valid!')

    return render(request, 'contact.html')
