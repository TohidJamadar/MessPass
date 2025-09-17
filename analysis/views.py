from .serializers import DataSerializer
from datetime import date
from stuapi.models import User
from .models import Data
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def get_count():
    user = User.objects.all()
    cnt=0
    for i in user:
        cnt+=i.daily_scan_count
    cnt=len(user)*2-cnt
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = days[date.today().weekday()] 
    data={"day":day, "count":cnt}
    try:
        instance = Data.objects.get(day=day)
        ser = DataSerializer(instance, data={"day": day, "count": cnt}, partial=True)
    except Data.DoesNotExist:
        ser = DataSerializer(data={"day": day, "count": cnt})
    if ser.is_valid():
        ser.save()
        print("data, is updated successfully !!")
        return
    print(ser.errors)


@csrf_exempt
def get(req):
    if(req.method=="GET"):
        data=Data.objects.all()
        ser=DataSerializer(data,many=True)
        return JsonResponse(ser.data,safe=False)
    return JsonResponse({"message":"only get method"})

    
