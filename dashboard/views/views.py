
from .metatrader5 import get_Deriv_Data, getICMarketsEU, getICMarketsEU1
from threading import Timer
from rest_framework.views import APIView
from ..serializer import DashboardSerializer
from rest_framework.response import Response
from ..models import AccountInfo
from rest_framework import status
from .error import *


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

t1 = RepeatTimer(10, get_Deriv_Data)
t2 = RepeatTimer(10, getICMarketsEU)
t3 = RepeatTimer(10, getICMarketsEU1)
t1.start()
t2.start()
t3.start()



class DashboardLogin1(APIView):

    def get(self, request, *args, **kwargs):
        try:
            info1 = AccountInfo.objects.all().filter(login= 68457740)
            serializerData = DashboardSerializer(info1, many= True)
            return Response(serializerData.data, status.HTTP_200_OK)
        except (exceptionError,ConnectionError):
            raise ConnectionError


class DashboardLogin2(APIView):

    def get(self, request, *args, **kwargs):
        try:
            info2 = AccountInfo.objects.all().filter(login = 68457577)
            serializerData = DashboardSerializer(info2, many= True)
            return Response(serializerData.data, status.HTTP_200_OK)
        except (exceptionError,ConnectionError):
            raise 
        


class DashboardLogin3(APIView):

    def get(self, request, *args, **kwargs):
        try:
            info3 = AccountInfo.objects.all().filter(login = 68457670)
            serializerData = DashboardSerializer(info3, many= True)
            return Response(serializerData.data, status.HTTP_200_OK)
        except (exceptionError,ConnectionError):
            raise ConnectionError


