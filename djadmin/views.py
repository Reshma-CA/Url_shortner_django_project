from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,logout
from django.views.decorators.cache import never_cache
from django.contrib import messages

# Create your views here.

# for admin login function

@never_cache
def adminlogin(request):

    if 'email' in request.session:
        return redirect('adminhome')


    
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        res=authenticate(request,email = email,password=password)
        if res is not None:
            request.session['emaile']=email # session creation
            return redirect('adminhome')
        else:
            
            messages.error(request,"Error in login! Invalid Login details!")
            return render(request,"adminlogin.html")

    return render(request,'adminlogin.html')

# for admin can view all details (firstname,lastname,email,shorturls) function
def adminhome(request):
    if "email" in request.session:
        datas = Register.objects.all()
        
    if request.method == "POST":
        enteredname = request.POST.get("searchitem")
        datas = Register.objects.filter(username__istartswith=enteredname)
        return render(request, "tadmin/users.html", {"datas": datas})
    else:
        return redirect('adminlogin')
    

# for admin logout function
def admin_logout(request):
    if 'email' in request.session:
        request.session.flush()
    return redirect('login')

 
