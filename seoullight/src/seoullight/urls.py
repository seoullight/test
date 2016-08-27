from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [
    url(r'^$', views.showRegistForm),
    url(r'^admin/', include(admin.site.urls)),
]


