from collections import UserString
import email
from mailbox import MaildirMessage
from operator import add
from turtle import Screen
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from napp.models import mobileCustamisation,buy
from django.contrib import messages


# Create your views here.
def home(request):
    id=request.session.get('cid')
    product_id=request.session.get("porduct_id")
  
    if id:
        id=int(id)
        user=User.objects.get(id=id)
        name=user.first_name
        if product_id:
            massage="your order successfully done for product id is ",product_id,"thanky you"
        else:
            massage="select your custmization"

    else:
        name="Gust"
        massage="select your custmization"
    context={'name':name,'massage':massage}
    return render(request,'index.html',context)    
def create_account(request):
    if request.method=='POST':
        frist_name=request.POST['frist_name']
        last_name=request.POST['last_name']
        email=request.POST['Email']
        Password=request.POST['Password']
        username=request.POST['Username']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username allready taken')
            return redirect('create_account')
        if User.objects.filter(email=email).exists():
            messages.info(request,'email allready taken')
            return redirect('create_account')
        user = User.objects.create_user(username=username,password=Password,email=email,last_name=last_name,first_name=frist_name)
        user.save()
        return redirect ('home')
   
    return render(request,'create_account.html')
  #user = User.objects.create_user(username=username,email=email,password=password,last_name=lname,first_name=fname)



def handel_login(request):
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)

            request.session['name']=username
            obj=User.objects.get(username=username)
            id=obj.id
            print(id)
            request.session['cid']=id
            return redirect ('custamization')
        else:
          
            return redirect('log')

     return render(request,"index.html")


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='log')

def select_custamization(request):
    name=request.session.get('name')
    obj=User.objects.get(username=name)
   
    if request.method=='POST':
        brand=request.POST.get('brand')
        size_of_screen=request.POST.get('size_of_screen')
        proceseor=request.POST.get('proceseor')
        ram=request.POST.get('ram')
        camera=request.POST.get('camera')
        customorID=obj.id
        obj=mobileCustamisation(brand=brand,size_of_screen=size_of_screen,proceseor=proceseor,ram=ram,camera=camera,customorID=customorID)
        obj.save()
        
        massage='your custamize mobile create'
        context={'massage':massage}
        return redirect('kart')
    return render(request,'select_custamization.html')


@login_required(login_url='log')
def kart(request):
     obj=request.session.get('name')
     id=request.session.get("cid")


     
      
     items=mobileCustamisation.objects.filter(customorID=id)
     
     context={'obj':obj,'items':items}
     return render(request,'kart.html',context)
@login_required(login_url='log')
def ordered (request):
    if request.method=="POST":
        id=request.POST.get("product")
        
        obj=mobileCustamisation.objects.filter(id=id)
        items=mobileCustamisation.objects.get(id=id)
        
        brand=items.brand
        if brand=="Apple":
            brand_prise=5000
        elif brand=='Lg':
            brand_prise=4000
        elif brand=='Google':
            brand_prise=4500
        elif brand=='Samsung':
            brand_prise=3000
        elif brand=='Sony':
            brand_prise=3500

        Screen=items.size_of_screen
        if Screen=="4inch":
            Screen_prise=1600
        elif Screen=='4.6inch':
             Screen_prise=2000
        elif Screen=='5inch':
             Screen_prise=3000
        elif Screen=='5.5inch':
             Screen_prise=3500
        elif Screen=='6inch':
             Screen_prise=4000

        camera=items.camera
        if camera=="8":
            camera_prise=1500
        elif camera=='12':
             camera_prise=2200
        elif camera=='16':
             camera_prise=2500
        elif camera=='32':
             camera_prise=3000
        elif camera=='64':
             camera_prise=3500
        
        processor=items.proceseor
        if processor=='Apple A14 Bionic':
            Processor_prise=10000
        elif processor=='Snapdragon 888':
            Processor_prise=5000
        elif processor=='Exynos 2100':
            Processor_prise=5500
        elif processor=='Kirin 9000':
            Processor_prise=8000
        elif processor=='Dimensity 9000':
            Processor_prise=8500

        total_prise=brand_prise+Screen_prise+camera_prise+Processor_prise
        request.session['prise']=total_prise
        request.session['pid']=items.id

        context={'obj':obj,'brand':brand,'brand_prise':brand_prise,'Screen_prise':Screen_prise,'camera_prise':camera_prise,'Processor_prise':Processor_prise,'total_prise':total_prise}
        return render(request,'ordered.html',context)
   
        
def brand(request):
    return render(request,"customization/brand.html")    
def ram(request):
    return render(request,"customization/ram.html") 
def camera(request):
    return render(request,"customization/camera.html") 
def processor(request):
    return render(request,"customization/processor.html") 
def screen(request):
    return render(request,"customization/screen.html") 


def log(request):
     
     return render(request,"log.html")

def Buy(request):
   
    
    
    if request.method=='POST':
         ##################################
        #customor id############
        name=request.session.get('name')
        obj=User.objects.get(username=name)
        cid=int(obj.id)
        prise=request.session.get('prise')
       
###############################################
          
        customorID=cid
        Address=request.POST.get('address')
        prise=prise
      
        productID=request.POST.get('product')
        obj=buy(productID=productID,customorID=customorID,Address=Address,prise=prise)
        
        obj.save()
        request.session['porduct_id']=productID
        return redirect("home")
        
    
    
             
