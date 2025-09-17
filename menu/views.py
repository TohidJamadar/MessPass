from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .models import Menu
from .serializers import MenuSerializer


@csrf_exempt
def update(req):
    if(req.method=='PUT'):
        data=JSONParser().parse(io.BytesIO(req.body))
        menu=Menu.objects.get(day=data.get('day'))
        ser=MenuSerializer(menu, data, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'msg':'data is updated !!'})
        return JsonResponse(ser.errors)
    return JsonResponse({'msg':'only put method is required !!'})

@csrf_exempt
def get(req):
    if req.method == "POST":
        data = JSONParser().parse(io.BytesIO(req.body))
        day = data.get("day")

        if not day:
            return JsonResponse({"error": "Missing day parameter"}, status=400)
        try:
            menu = Menu.objects.get(day=day)
            serializer = MenuSerializer(menu)
            return JsonResponse(serializer.data, safe=False)
        except Menu.DoesNotExist:
            return JsonResponse({"error": "day not found"}, status=404)