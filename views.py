import json
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import django.core.serializers as serializer
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

def companylogin_validation(request,company_name, company_password):

    try:
        company = Company.objects.get(company_name=company_name)
        if company.company_password == company_password:
            content = {
                'company_name': company_name
            }
            return JsonResponse(content)

    except Exception:
        return HttpResponse("Company not Found")

    return HttpResponse("Company not Found")


def register_company(request):
    data = json.loads(request.body.decode('utf-8'))
    User.objects.create(
        company_name=data['company_name'],
        company_password=data['company_password'],
        name=data['name'],
        location=data['location'],
        nOfEmployees=data['nOfEmployees'],
        email=data['email'],
        company_interests=data['company_interests'])

    return HttpResponse("Company_Added")

def get_users(request):
    try:
        user = User.objects.all()
        data = serializer.serialize('json', user)
        return HttpResponse(data, content_type='application.json')

    except Exception:
        return HttpResponse ("No users")

    return HttpResponse("No users")
