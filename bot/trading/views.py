from django.shortcuts import render


def get(request):
    return render(request, 'index.html')
