from .utils import getAllZipcodes
from .serializers import DidTheyMoveSerializer, CheckMovedSerializer, ClientlistSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from django.contrib.auth.models import User
from .models import *

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import response, status, views, viewsets, generics
from django.shortcuts import render


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

    # @api_view(['POST'])
    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            didTheyMove = DidTheyMove.objects.filter(customer=serializer.validated_data['customer'], address=serializer.validated_data['address'], zipCode=serializer.validated_data['zipCode'], client=serializer.validated_data['client'])
            print(len(didTheyMove))
            if len(didTheyMove) == 0:
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


class ClientlistView(viewsets.ModelViewSet):

    serializer_class = ClientlistSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            headers = self.get_success_headers(serializer.data)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        'api/didTheyMove'
    ]
    return response.Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return response.Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return response.Response({'response': data}, status=status.HTTP_200_OK)
    return response.Response({}, status.HTTP_400_BAD_REQUEST)

