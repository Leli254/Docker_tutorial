from django.urls import path
from . import views

app_name = 'sales'


urlpatterns = [
    #path('', views.sales_data_view, name='sales_data_view'),
    path('', views.SalesDataView.as_view(), name='sales_data_view_class'),
]