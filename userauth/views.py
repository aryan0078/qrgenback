from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Users
from .serealizers import UsersSerializer
@csrf_exempt
@api_view(["POST"])
def login(request):
    
       
    s=Users.objects.get(email=request.data['email'])
        
    ser=UsersSerializer(s)
    return Response(ser)
    #if ser.data["password"]==request.data['password'] and ser.data['email']==request.data['email']:
       # return Response({"data":ser.data,"msg":"Login Done!"})
        #return JsonResponse({"msg":"Username or password is incorrect"})
   
       # return JsonResponse({"msg":"User not found"})
@csrf_exempt
@api_view(["POST"])
def signup(request):
    try:
        ser=UsersSerializer(data=request.data)
        
        if ser.is_valid():
            ser.save()
            return JsonResponse({'data':ser.data,'msg':"Signup Done!"})
        return JsonResponse({"msg":"Already Registerd"})
        
    except:
        return JsonResponse({'msg':"Something is missing"})
        