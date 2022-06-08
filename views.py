from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'services/contact.html')

def about(request):
    return render(request,'services/about.html')    