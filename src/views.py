from django.shortcuts import render,redirect


def index(request):
    return render(request, 'index.html', {

    })

def load_page(request,template_name):
    return render(request, f'{template_name}', {

    })