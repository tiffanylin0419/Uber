from django.shortcuts import render, redirect

# Create your views here.

# accounts/views.py
from django.contrib import messages
from .form import SignupForm  

    
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