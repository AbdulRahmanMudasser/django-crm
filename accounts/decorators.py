from django.contrib import messages
from django.shortcuts import redirect

# Unauthenticated User Decorator
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Check if User is Authenticated
        if request.user.is_authenticated:
            # Dispaly Message
            messages.info(request, 'You Are Already Logged In')
            
            # Redirect User to Home Page or Restrict User From Accessing Login or Register Page
            return redirect('home')
        
        else: 
            # Allow User to Access View
            return view_func(request, *args, **kwargs)
        
    return wrapper_func
        
        
        