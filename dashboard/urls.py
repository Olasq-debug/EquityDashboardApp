from django.urls import path 
from .views.views import DashboardLogin1, DashboardLogin2, DashboardLogin3

urlpatterns = [
    path('logindata1/', DashboardLogin1.as_view(), name= 'logindata1'),
    path('logindata2/', DashboardLogin2.as_view(), name= 'logindata2'),
    path('logindata3/', DashboardLogin3.as_view(), name= 'logindata3'),

]
