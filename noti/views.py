from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .models import Noti
from .serializers import NotiSerializer


@csrf_exempt
def update(req):
    if(req.method=='PUT'):
        data=JSONParser().parse(io.BytesIO(req.body))
        noti=Noti.objects.get(date=data.get('date'))
        ser=NotiSerializer(noti, data, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'msg':'data is updated !!'})
        return JsonResponse(ser.errors)
    return JsonResponse({'msg':'only put method is required !!'})

@csrf_exempt
def post(req):
    if(req.method=='POST'):
        data=JSONParser().parse(io.BytesIO(req.body))
        ser=NotiSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'msg':'data is created !!'})
        return JsonResponse(ser.errors)
    return JsonResponse({'msg':'only post method is applicable !!'})

@csrf_exempt
def get(req):
    if req.method == "POST":
        notis = Noti.objects.all().order_by('-date')  # newest first
        serializer = NotiSerializer(notis, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def delete(req):
    if(req.method=="DELETE"):
        data=JSONParser().parse(io.BytesIO(req.body))
        date=data.get('date')
        noti=Noti.objects.get(date=date)
        noti.delete()
        return JsonResponse({'msg':'noti is deleted succefully !!'})
    return JsonResponse({'msg':'only delete method is applicable'})
