from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chatbot.html')


def register(request):
    return render(request,"register.html")

def sigin(request):
    return render(request,"login.html")