from django.http import HttpResponse

## this function will handle our main
## welcome messgae

def welcome(request):
    return HttpResponse("hello world")