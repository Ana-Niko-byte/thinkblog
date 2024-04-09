from django.shortcuts import render
from .models import Creator
from django.http import HttpResponse
# Create your views here.

def about_page(request):
    author = Creator.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {'about' : author},
    )