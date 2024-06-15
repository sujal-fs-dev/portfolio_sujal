from django.shortcuts import render, redirect
from datetime import datetime
from base.models import Form

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact_v(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        

        form = Form(name=name, email=email, desc=desc, date=datetime.today())
        form.save()  # Corrected save method call

        # Redirect to a new URL or render a success template/message
        return redirect('contact')  # Redirect to home page after submission
        # Or use render to show a success message on the same page
        # return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


