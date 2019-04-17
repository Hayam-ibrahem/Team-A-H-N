import json
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .models import Company

def login_validation(request,user_name, user_password):

    try:
        user = User.objects.get(user_name=user_name)
        if user.password == user_password:
            content = {
                'user_name': user_name
            }
            return JsonResponse(content)

    except Exception:
        return HttpResponse("User not Found")

    return HttpResponse("User not Found")

@csrf_exempt
def register_user(request):
    
    data = json.loads(request.body.decode('utf-8'))
    User.objects.create(
                        user_name=data['user_name'],
                        password=data['password'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        age=data['age'],
                        gender=data['gender'],
                        interests=data['interests'])

    return HttpResponse("User_Added")


