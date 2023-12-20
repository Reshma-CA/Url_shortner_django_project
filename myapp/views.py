from django.shortcuts import render
from django.shortcuts import render,redirect
import re
from myapp. models import Register,Url
from django.contrib.auth import authenticate
from django.contrib import messages

from django.views.decorators.cache import never_cache


# Create your views here.

def register(request):
    
    if request.method=="POST":
        error={}
        Firstname=request.POST.get("Lastname")
        Lastname=request.POST.get("Lastname")
        email=request.POST.get("email")
        
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")

        
        if not Firstname.isalpha():
           error["Lastname"]="Firstname Required!"
        elif not Lastname.isalpha() :
            error["Lastname"]="Lastname required!"
        
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            error["email"]="Invalid Email"

        elif Register.objects.filter(email=email):
            error["email"]="Email already exists! Please Use a different email"

        elif len(password)<6:
            
            error["password"]="Password must atleast contain 1 characters"

        elif len(password)>8:
            
            error["password"]="Password can only have upto 8 characters"
            
        elif password!=confirmpassword:
            
            error["repassword"]="Passwords doesn't match to Confirm password!" 

         
        else:
           
            res=Register(Firstname=Firstname,email=email,password=password,confirmpasswordd=confirmpassword,Lastname=Lastname)
            res.save()
            
            msg="Signup Successfull"
            return redirect('login')

    return render(request,'register.html')

# for login page function

@never_cache
def login(request):
    if 'email' in request.session:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            request.session['email'] = email
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# for url page function
@never_cache
def home(request):
    context = {}
    if request.method == 'POST':
        original_url = request.POST['original_url']
        url = Url.objects.create(original_url=original_url)
        short_url = request.build_absolute_uri('/') + url.short_code
        context['short_url'] = short_url

    return render(request, 'url.html', context)

def redirect_to_original(request, short_code):
    url = Url.objects.get(short_code=short_code)
    return redirect(url.original_url)

# for user logout function

def logout(request):
    
    if 'email' in request.session:
        request.session.flush()
    return redirect('login')


