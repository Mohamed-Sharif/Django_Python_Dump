from django.shortcuts import render

def contact_us(request):
    return render(request, 'contactus/contact_us.html')
