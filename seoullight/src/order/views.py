from django.shortcuts import render_to_response
from order.models import Customer, testOrder
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def showRegistForm(request):
    return render_to_response('order/register/register.html')

@csrf_exempt
def DoWriteRegistInfo(request):
    br = Customer(
        eMail = request.POST['eMail'],
        password = request.POST['password'],
        gender = request.POST['gender'],
        nation = request.POST['nation'],
        age = request.POST['age'],
    )
    
    br.save()
    
    url = '/showLoginForm'
    return HttpResponseRedirect(url)

def showLoginForm(request):
    return render_to_response('order/login/login.html')

@csrf_exempt
def login(request):
    m = Customer.objects.get(eMail=request.POST['eMail'])
    if m.password == request.POST['password']:
        request.session['eMail'] = m.eMail
        
        userInfo = m.eMail
        print(userInfo)
        return render_to_response('order/service/order/insertOrderInfo.html', {'userInfo':userInfo})
    else:
        return HttpResponse("Your username and password didn't match.")

@csrf_exempt
def DoWriteOrderInfo(request):
    br = testOrder(
        eMail = request.POST['eMail'],
        state = request.POST['state'],
        destination = request.POST['destination'],
        customerName = request.POST['customerName'],
        baggageKind = request.POST['baggageKind'],
        quantity = request.POST['quantity'],
    )
    
    br.save()