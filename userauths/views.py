from django.shortcuts import redirect,render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from userauths.models import User
from django.http import JsonResponse

# User=settings.AUTH_USER_MODEL

def register_view(request):
    
    if request.method=='POST':
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Hey {username}, Your account has been registered")
            new_user= authenticate(username=form.cleaned_data['email'],
                                   password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")
    else:
        form=UserRegisterForm()
        
        
    context={
        'form': form,
    }
    return render(request,"userauths/sign-up.html", context)

def login_view(request):
    request.session['order_placed'] = True
    if request.user.is_authenticated:
        messages.warning(request,"Hey you are already logged in")
        return redirect("core:index")
    
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        try:
            user=User.objects.get(email=email)
            user=authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request,"You logged in successfully")
                return redirect("core:index")
            else:
                messages.warning(request,"User does not exist. Create an account")
        except:
            messages.warning(request,f"User with {email} does not exist")
            
        
            
 
    
    return render(request,"userauths/sign-in.html")


def logout_view(request):
    logout(request)
    messages.success(request,"You logged out")
    return redirect("userauths:sign-in")

def shop_view(request):
    return render(request,"userauths/shop.html")

def blog_view(request):
    return render(request,"userauths/blog.html")

def about_view(request):
    return render(request,"userauths/about.html")

def contact_view(request):
    return render(request,"userauths/contact.html")

@login_required
def checkout_view(request):
    return render(request, "userauths/checkout.html")