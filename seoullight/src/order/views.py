from django.shortcuts import render_to_response

def showRegistForm(request):
    return render_to_response('order/register/register.html')