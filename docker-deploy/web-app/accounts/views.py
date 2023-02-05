from django.shortcuts import render, redirect

# Create your views here.

# accounts/views.py
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from django.http import HttpResponse  
from .form import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  

from django.contrib.auth import get_user_model


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"
    
def signup(request):  
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You have successfully signed up!')
            return redirect('login')
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form}) 
  