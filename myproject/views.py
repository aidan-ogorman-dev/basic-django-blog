#from django.http import HttpResponse
from django.shortcuts import render

# user = aidan
# pwd = adminuser
def homepage(request):
    # return HttpResponse("Hello World! I'm home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("My About Page")
    return render(request, 'about.html')
