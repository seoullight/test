from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [
    url(r'^$', views.showRegistForm),
    url(r'^DoWriteRegistInfo/$', views.DoWriteRegistInfo),
    url(r'^showLoginForm/$', views.showLoginForm),
    url(r'^login/$', views.login),
    url(r'^DoWriteOrderInfo/$', views.DoWriteOrderInfo),
    url(r'^admin/', include(admin.site.urls)),
]


