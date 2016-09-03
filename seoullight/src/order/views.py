from django.shortcuts import render_to_response
from order.models import testOrder
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def showRegistForm(request):
    return render_to_response('order/register/register.html')

@csrf_exempt
def DoWriteRegistInfo(request):
    br = User(
        email = request.POST['email'],
        password = request.POST['password'],
        username = request.POST['username'],
    )
    
    br.save()
    
    url = '/showLoginForm'
    return HttpResponseRedirect(url)

def showLoginForm(request):
    return render_to_response('order/login/login.html')

@csrf_exempt
def login(request):
    loginUser = User.objects.get(email=request.POST['email'])
    if loginUser.password == request.POST['password']:
        request.session['email'] = loginUser.email
        
        userInfo = loginUser.email
        print(userInfo)
        return render_to_response('order/service/order/insertOrderInfo.html', {'userInfo':userInfo})
    else:
        return HttpResponse("Your username and password didn't match.")

@csrf_exempt
def DoWriteOrderInfo(request):
    br = testOrder(
        email = request.POST['email'],
        state = request.POST['state'],
        destination = request.POST['destination'],
        customerName = request.POST['customerName'],
        baggageKind = request.POST['baggageKind'],
        quantity = request.POST['quantity'],
    )
    
    br.save()
    
    url = '/showOrderList'
    return HttpResponseRedirect(url)

@csrf_exempt
def showOrderList(request):
    return render_to_response('order/service/order/orderList.html')