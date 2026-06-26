from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")

def contact(request):
    return HttpResponse("Contact us")

def about(request):
    return HttpResponse("About Us")

