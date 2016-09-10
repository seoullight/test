from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [
    url(r'^$', views.showLoginForm),
    url(r'^DoWriteRegistInfo/$', views.DoWriteRegistInfo),
    url(r'^showLoginForm/$', views.showLoginForm),
    url(r'^showRegistForm/$', views.showRegistForm),
    url(r'^login/$', views.login),
    url(r'^showInsertOrderInfoView/$', views.showInsertOrderInfoView),
    url(r'^showSelectServiceView/$', views.showSelectServiceView),
    url(r'^DoWriteOrderInfo/$', views.DoWriteOrderInfo),
    url(r'^showOrderList/$', views.showOrderList),
    url(r'^showOrderDetail/$', views.showOrderDetail),
    url(r'^duplicationCheck/$', views.duplicationCheck),
    url(r'^admin/', include(admin.site.urls)),
]