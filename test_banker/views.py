from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


def index(request):
    print(request.user)
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):

    return render(request, "contact.html")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
