from django.urls import path
from .views import  CusipCode
app_name = 'openfigi'

urlpatterns = [
    path('', CusipCode.as_view() , name='cusip')
]
