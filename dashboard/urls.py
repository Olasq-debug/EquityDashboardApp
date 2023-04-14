from django.urls import path 
from .views.views import Index

urlpatterns = [
    path('logindata1/', Index, name= 'logindata1'),
    # path('logindata2/', DashboardLogin2.as_view(), name= 'logindata2'),
    # path('logindata3/', DashboardLogin3.as_view(), name= 'logindata3'),

]
