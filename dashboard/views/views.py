
from .metatrader5 import get_Deriv_Data, getICMarketsEU, getICMarketsEU1
from threading import Timer
#from rest_framework.views import APIView
#from ..serializer import DashboardSerializer
from rest_framework.response import Response
#from ..models import AccountInfo
#from rest_framework import status
from .error import *
from django.shortcuts import render
import utils




class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

t1 = RepeatTimer(60, get_Deriv_Data)
t2 = RepeatTimer(60, getICMarketsEU)
t3 = RepeatTimer(60, getICMarketsEU1)
t1.start()
t2.start()
t3.start()



def Index(request):
    data1 = utils.myCollection.find({"login" : 68457740})
    data2 = utils.myCollection.find({"login" : 68457577})
    data3 = utils.myCollection.find({"login" : 68457670})
    context = {
        "data1s": data1,
        "data2s": data2,
        "data3s": data3
    }
    return render(request, "../template/index.html", context)

# class Dashboard(APIView):
#     def get(self, request, *args, **kwargs):
#         post = AccountInfo.objects.all()
#         dataSerializer = DashboardSerializer(post, many=True)
#         Response(dataSerializer.data, status.HTTP_200_OK)



