from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create a simple view that take a request and return a response
def say_hello(request):
    return HttpResponse("Hello Django!")



def run_template(request):
    username = ""
    if request.method == "POST":
        username = request.POST.get("username")
    return render(request, "index.html", {"username": username})


