from django.conf.urls import url

from . import views

app_name = 'gateway_app'
urlpatterns = [
    url(r'^rate/', views.rate, name = 'rate'),
    url(r'^data/', views.data, name = 'data'),

]