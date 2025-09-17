import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings


@csrf_exempt
def update(req):
    if(req.method=='PUT'):
        data=JSONParser().parse(io.BytesIO(req.body))
        user=User.objects.get(id=data.get('id'))
        ser=UserSerializer(user, data, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'msg':'data is updated !!'})
        return JsonResponse(ser.errors)
    return JsonResponse({'msg':'only put method is required !!'})

@csrf_exempt
def post(req):
    if(req.method=='POST'):
        data=JSONParser().parse(io.BytesIO(req.body))
        ser=UserSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'msg':'data is created !!'})
        return JsonResponse(ser.errors)
    return JsonResponse({'msg':'only post method is applicable !!'})


@csrf_exempt
def verify(req):
    if req.method == 'POST':
        data = JSONParser().parse(io.BytesIO(req.body))
        email = data.get("email")
        if not email:
            return JsonResponse({'msg': 'Email is required'}, status=400)
        otp = str(random.randint(100000, 999999))
        try:
            send_mail(
                subject="Your Verification OTP",
                message=f"Your OTP is {otp}. It is valid for 10 minutes.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({'msg': 'Failed to send OTP', 'error': str(e)}, status=500)
        return JsonResponse({'msg': 'OTP sent successfully!', 'otp': otp})
    return JsonResponse({'msg': 'Only POST method is allowed'}, status=405)


@csrf_exempt
def delete(req):
    if(req.method=="DELETE"):
        data=JSONParser().parse(io.BytesIO(req.body))
        id=data.get('id')
        user=User.objects.get(id=data.get('id'))
        user.delete()
        return JsonResponse({'msg':'user is deleted succefully !!'})
    return JsonResponse({'msg':'only delete method is applicable'})

@csrf_exempt
def get(req):
    if req.method == "POST":
        data = JSONParser().parse(io.BytesIO(req.body))
        email = data.get('email')
        password = data.get('password')

        if (not email and not password):
            return JsonResponse({"message": "Email and password are required"}, status=400)

        try:
            user = User.objects.get(email=email, password=password)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False, status=200)
        except User.DoesNotExist:
            return JsonResponse({"message": "Invalid email or password"}, status=401)
    return JsonResponse({"message": "Invalid request method"}, status=405)

def reset_scan_count():
    User.objects.all().update(daily_scan_count=2)


def get_finished_plate_count(req):
    if req.method=="GET":
        user = User.objects.all()
        cnt=0
        for i in user:
            cnt+=i.daily_scan_count
        cnt=len(user)*2-cnt
        return JsonResponse({"cnt":cnt})

