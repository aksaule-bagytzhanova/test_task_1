import api
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status
from .serializers import Areas1Serilizer, Areas2Serilizer
from .models import Area1Model, Area2Model
# Create your views here.



@api_view(['GET'])
def ShowAll(request):
    areas1 = Area1Model.objects.all()
    areas2 = Area2Model.objects.all()
    serializer1 = Areas1Serilizer(areas1, many=True)
    serializer2 = Areas2Serilizer(areas2, many=True)

    Serializer_list = [serializer1.data, serializer2.data]

    content = {
        'status': 1, 
        'responseCode' : status.HTTP_200_OK, 
        'data': Serializer_list,

        }
    return Response(content)

@api_view(['GET'])
def ViewArea1(request, pk):
    areas1 = Area1Model.objects.get(id=pk)
    serializer1 = Areas1Serilizer(areas1, many=False)
    return Response(serializer1.data)

@api_view(['GET'])
def ViewArea2(request, pk):
    areas2 = Area2Model.objects.get(id=pk)
    serializer2 = Areas2Serilizer(areas2, many=False)
    return Response(serializer2.data)


@api_view(['POST'])
def CreateArea1(request):
    serializer = Areas1Serilizer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def CreateArea2(request):
    serializer = Areas2Serilizer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UpdateArea1(request, pk):
    area = Area1Model.objects.get(id=pk)
    serializer = Areas1Serilizer(instance=area, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateArea2(request, pk):
    area = Area2Model.objects.get(id=pk)
    serializer = Areas2Serilizer(instance=area, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def DeleteArea1(request, pk):
    area = Area1Model.objects.get(id=pk)
    area.delete()

    return Response('Items delete successfully!')

@api_view(['GET'])
def DeleteArea2(request, pk):
    area = Area2Model.objects.get(id=pk)
    area.delete()

    return Response('Items delete successfully!')