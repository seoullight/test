from datetime import datetime
from django.utils import formats
from django.shortcuts import render_to_response
from order.models import Order, Customer, DeliveringState
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def showRegistForm(request):
    return render_to_response('order/register/register.html')

@csrf_exempt
def DoWriteRegistInfo(request):
    br = Customer(
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
    loginUser = Customer.objects.get(email=request.POST['email'])
    if loginUser.password == request.POST['password']:
        request.session['email'] = loginUser.email
        
        userInfo = loginUser.email
        userPkId = loginUser.id
        print(userInfo)
        return render_to_response('order/service/order/insertOrderInfo.html', {'userInfo':userInfo, 'userPkId':userPkId})
    else:
        return HttpResponse("Your username and password didn't match.")

@csrf_exempt
def DoWriteOrderInfo(request):
    
    userPkId = request.POST['userPkId']
    orderDateTime = datetime.now()
    formatted_datetime = formats.date_format(orderDateTime, "SHORT_DATETIME_FORMAT")
    mixedOrderNumber = formatted_datetime + userPkId
    
    user = Customer.objects.get(email=request.POST['email'])
    
    state = DeliveringState.SHIPPED
    
    br = Order(
        customer = user,
        deliveringState = state,
        orderNumber = mixedOrderNumber,
        destination = request.POST['destination'],
        baggageKind = request.POST['baggageKind'],
        customerName = request.POST['customerName'],
        quantity = request.POST['quantity'],
    )
    
    br.save()
    
    url = '/showOrderList'
    return HttpResponseRedirect(url)

@csrf_exempt
def showOrderList(request):
    return render_to_response('order/service/order/orderList.html')