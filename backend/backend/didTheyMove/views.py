from django.shortcuts import render
from .utils import getAllZipcodes
from .serializers import DidTheyMoveSerializer, CheckMovedSerializer
from .models import DidTheyMove
from rest_framework import response, status, views, viewsets
import http.client
from .models import *

# Create your views here.

# def call_my_function():
#     conn = http.client.HTTPSConnection("api.gateway.attomdata.com")
#     headers = { 
#         'accept': "application/json", 
#         'apikey': "8c7cae441f145b29c01026729f6aa409", 
#     } 

#     conn.request("GET", "/propertyapi/v1.0.0/saleshistory/expandedhistory?address1=4529%20Winona%20Court&address2=Denver%2C%20CO", headers=headers) 

#     res = conn.getresponse() 
#     data = res.read() 

#     print(data.decode("utf-8"))

class DidTheyMoveView(viewsets.ModelViewSet):
    serializer_class = DidTheyMoveSerializer
    queryset = DidTheyMove.objects.all()
    print("hello")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckMovedView(views.APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs['client_name'])
        getAllZipcodes(kwargs['client_name'])
        return response.Response("", status=status.HTTP_201_CREATED, headers="")
