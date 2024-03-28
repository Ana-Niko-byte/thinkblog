from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def main(response):
#     if response.method == 'GET':
#         return HttpResponse('Hey there :)')
#     else:
#         return response
def my_blog(request):
    return HttpResponse("Hello, Blog!")