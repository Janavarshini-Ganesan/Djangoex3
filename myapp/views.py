from django.shortcuts import render, redirect 
from .forms import UserRegistrationForm 

def register(request): 
    if request.method == 'POST': 
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): 
            user = form.save()  # Save the user and capture the user object 
            username = user.username  # Get the username from the saved user 
            return redirect('success', username=username)  # Redirect to success view 
    else: 
        form = UserRegistrationForm() 
    return render(request, 'signup.html', {'form': form}) 

def success(request, username): 
    return render(request, 'success.html', {'username': username})
