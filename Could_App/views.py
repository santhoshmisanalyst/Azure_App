from django.shortcuts import render
from django.http import HttpResponse


def members(request):
    
    return render(request, 'Login.html')
    #return HttpResponse("Hello world! Bolgam Santhosh Goud and Sadhika ")