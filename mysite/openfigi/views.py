from django.shortcuts import render
from .models import Cusip
from .serializers import CusipSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from  openfigi.openfigiFunction import start 
from .models import CusipForm 
from datetime import datetime
# Create your views here.

class CusipCode(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'openfigi/home.html'

    def get(self, request):

        try:
            queryset = Cusip.objects.all()
            serializer = CusipSerializers(data=queryset)
        except AttributeError:
            queryset = {}
        return Response({'openfigi': queryset})

    def post(self, request, format=None):
        f = CusipForm(request.POST)
        job_results = start.map_jobs(f.data['cusipCode'])
        cusipCode = f.data['cusipCode']
        print('job_results : ',job_results)

        if 'error' not in  job_results[0]:
            if 'Muni' in job_results[0]['data'][0].values():
                Cusip.objects.create(   cusipCode=cusipCode, name= job_results[0]['data'][0]['name'], 
                                        ticker = job_results[0]['data'][0]['ticker'],
                                        marketSector=job_results[0]['data'][0]['marketSector'],
                                        securityType=job_results[0]['data'][0]['securityType'],
                                        exchCode=job_results[0]['data'][0]['exchCode'],
                                        timeStamp=datetime.now()).save()
            else:
                print('\n\n\nNo Municpal\n\n\n')
        else:
                print('\n\n\nNot a Cusip Code\n\n\n')

        queryset = Cusip.objects.all()

        return Response({'openfigi': queryset})