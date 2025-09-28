from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    print(request.user)
    return render(request, "index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:

    return render(request, "contact.html")
