from django.http import HttpResponse
from django.shortcuts import render
## this function will handle our main
## welcome messgae

def welcome(request):
    return render(request,'tictactoe/welcome.html')