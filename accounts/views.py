
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import  send_mail
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from .utils import token_gen
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from decouple import config
from config.africanstalking_config import sms

from .forms import LoginForm, RegistrationForm
User = get_user_model()

"""for threading function where a user 
is told a function is complete while still loading
"""
import threading

import africastalking

username = "vax"
api_key = config('API_KEY')
africastalking.initialize(username, api_key)

     
   
def LogInView(request, *args, **kwargs):
    next_page = request.GET.get('next')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if next_page is not None:  
                        return HttpResponseRedirect(next_page)
                    return redirect('core:index')
                messages.error(request,"invalid Login! Try again")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)

def LogOutView(request, *args, **kwargs):
    logout(request)
    messages.success(request,"You successfully logged out")
    return redirect('core:index')

def RegisterView(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = user.phone
            
            # pass phone to session
            request.session['phone'] = phone

            sms_content = f"Your verification code is {user.ver_code}"
            sms.send(sms_content, [phone])
            messages.info(request, "A verification code has been sent to your phone number")
            return redirect('accounts:phone-verification')
        print(form.errors)
        return render(request, 'auth/register.html')
            
    return render(request, 'auth/register.html', {'form': form})

def VerificationView(request,uidb64, token):

    uidb = force_str(urlsafe_base64_decode(uidb64)) or None
    user = User.objects.get(pk=uidb) or None

        
    if user is not  None and token_gen.check_token(user, token):
        user.is_active=True
        user.save()
        messages.info(request, "account activated successfully")  
        return redirect("accounts:login")
    return render(request,'auth/activation_failed.html')


def RequestResetEmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
    
        user = User.objects.filter(email=email)
    
        if user.exists():
            uidb64 = urlsafe_base64_encode(force_bytes(user[0].pk))
            domain = get_current_site(request).domain #gives us the domain
            link = reverse('accounts:reset-password', 
                            kwargs={
                                'uidb64':uidb64, 
                                'token':PasswordResetTokenGenerator().make_token(user[0])
                                    })
            reset_password_url = f"http://{domain+link}"
            
            mail_subject = "Reset Password"

            
            mail_body = f"hi {user[0].username} click the link below to reset your password\n {reset_password_url}"
            mail = send_mail (mail_subject, mail_body,'noreply@courses.com',[email], fail_silently=False)
            messages.success(request, "Check your Email for the reset link")
            return redirect('accounts:login')
        else:
            messages.error(request, "Sorry, there is no user with that email")
            return redirect('accounts:request-reset-email')

    return render(request, 'auth/reset_email_form.html', {})
  
def ResetPasswordView(request, uidb64, token):
    
    if request.method == 'POST':
        context = {
            'uidb64':uidb64,
            'token':token,
        }
        
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        
        if password1 == "":
            messages.error(request, "Password is required")
        if password2 == "":
            messages.error(request, "Repeat Password is required")
            return render(request, 'auth/reset_password.html', context)
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        if len(password1)<6:
            messages.error(request,"Password is too short")
            return render(request, 'auth/reset_password.html', context)
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        if len(password1)<6:
            messages.error(request,"Password is too short")
            return render(request, 'auth/reset_password.html', context)  
        
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password1)
            user.save()
            messages.success(request, "password changed successfully")
            return redirect('accounts:login')
        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, "oops! something went wrong")
            return render(request, 'auth/reset_password.html', context)
        
    context = {
        'uidb64':uidb64, 
        'token':token
        }
        
    try:
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
        
        if not PasswordResetTokenGenerator().check_token(user, token):
            messages.error(request, "Opps, The link has expired")
            return render(request, 'auth/reset_email_form.html')
        
        messages.success(request, "verified")
        return render(request, 'auth/reset_password.html', context)
    except DjangoUnicodeDecodeError as identifier:
        messages.error(request, "oops! something went wrong")
        return render(request, 'auth/reset_email_form.html', context)