from django.shortcuts import render
from .models import Creator
from .forms import CollaborateForm
from django.contrib import messages
# Create your views here.

def about_page(request):
    if request.method == 'POST':
        print('received collaboration request')
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            c_form = collaborate_form.save(commit=False)
            c_form.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Collaboration request received! I endeavour to respond within 2 working days.'
    )
    author = Creator.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {'about' : author, 
         "collaborate_form": collaborate_form,}
    )