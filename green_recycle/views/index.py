from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")


def home1(request):
    return render(request, "index-1.html")

def home2(request):
    return render(request, "index-2.html")


def home3(request):
    return render(request, "index-3.html")


def home4(request):
    return render(request, "index-4.html")
