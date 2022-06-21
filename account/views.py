from rest_framework.response import Response
from rest_framework.decorators import api_view
from account import serilizers
from .models import EmpData
from account.serilizers import EmpDataSerializer

# Create your views here.

@api_view(['GET'])
def APIoverview(request):
    return Response('API calling')

@api_view(['GET'])
def EmpList(request):
    emp=EmpData.objects.all()
    serilizer=EmpDataSerializer(emp,many=True)
    return Response(serilizer.data)

@api_view(['POST'])
def EmpCreate(request):
    serilizer=EmpDataSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)

@api_view(['POST'])
def EmpUpdate(request,pk):
    emp=EmpData.objects.get(pk=pk)
    serilizer=EmpDataSerializer(instance=emp,data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)
@api_view(['DELETE'])
def EmpDelete(request,pk):
    serilizer=EmpData.objects.get(pk=pk)
    serilizer.delete()
    return Response("Data deleted sucessfully")





