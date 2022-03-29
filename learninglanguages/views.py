from django.shortcuts import render


def index(request):
    return render(request, 'languages/index.html')

def html5language(request):
    return render(request, 'languages/html5language.html')

def pythonlanguage(request):
    return render(request, 'languages/pythonlanguage.html')

