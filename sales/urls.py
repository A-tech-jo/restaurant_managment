from django.urls import path,include
from sales import views



urlpatterns = [
     path('', include('sales.Customer.urls')), 
    path('SalesListJson/', views.SalesListJson.as_view(),name="SalesListJson"),
     path('SalesInvoice', views.SalesInvoice.as_view(),name='SalesInvoice'),
     path('get_code/', views.get_code, name='get_code'),

]
