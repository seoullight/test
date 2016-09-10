from datetime import datetime

from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import get_template
from django.utils import formats
from django.views.decorators.csrf import csrf_exempt

from order.models import Order, Customer, DeliveringState


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
        return render_to_response('order/service/selectService.html', {'userInfo':userInfo, 'userPkId':userPkId})
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
    loginUserEmail = request.session['email']
    allOrderList = list(Order.objects.all())
    orderList = list()
    for order in allOrderList:
        if order.customer.email == loginUserEmail:
            orderList.append(order)
    
    return render_to_response('order/service/order/orderList.html', {'orderList':orderList})

@csrf_exempt
def showOrderDetail(request):
    sendedOrderNumber = request.POST['orderNumber']
    order = Order.objects.get(orderNumber=sendedOrderNumber)
    orderStatus = order.deliveringState
    
    return render_to_response('order/service/order/orderDetail.html', {'orderNumber':sendedOrderNumber, 'orderStatus':orderStatus})

@csrf_exempt
def duplicationCheck(request):
        
    email = request.GET['email']
    if Customer.objects.filter(email=email).exists():
        duplicated = True
    else:
        duplicated = False
    return HttpResponse(duplicated)

@csrf_exempt
def showInsertOrderInfoView(request):
    loginUserEmail = request.session['email']
    loginUser = Customer.objects.get(email=loginUserEmail)
    userPkId = loginUser.id
    return render_to_response('order/service/order/insertOrderInfo.html', {'loginUserEmail': loginUserEmail, 'userPkId':userPkId})

@csrf_exempt
def showSelectServiceView(request):
    return render_to_response('order/service/selectService.html')
