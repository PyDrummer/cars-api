from django.urls import path
from .views import CarList, CarDetail

urlpatterns = [
    path('', CarList.as_view(), name='cars_list'),
    path('', CarDetail.as_view(), name='cars_detail')
]