import json
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import django.core.serializers as serializer
from .models import User
from .models import Company

@csrf_exempt
def validateLogin(request,user_name, user_password):

    try:
        user = User.objects.get(user_name=user_name)
        if user.password == user_password:
            content = {
                'user_ID': user.pk
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

@csrf_exempt
def companylogin_validation(request,company_name, company_password):

    try:
        company = Company.objects.get(company_name=company_name)
        if company.company_password == company_password:
            content = {
                'company_ID': company.pk
            }
            return JsonResponse(content)

    except Exception:
        return HttpResponse("Company not Found")

    return HttpResponse("Company not Found")

@csrf_exempt
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

@csrf_exempt
def get_users(request):
    try:
        user = User.objects.all()
        data = serializer.serialize('json', user)
        return HttpResponse(data, content_type='application.json')

    except Exception:
        return HttpResponse ("No users")

    return HttpResponse("No users")

@csrf_exempt
def get_companys(request):
    try:
        company = Company.objects.all()
        data = serializer.serialize('json', company)
        return HttpResponse(data, content_type='application.json')

    except Exception:
        return HttpResponse ("No companys")

    return HttpResponse("No companys")

@csrf_exempt
def userByID(request,user_ID):
    try:
        user = User.objects.get(pk=user_ID)
        data = serializer.serialize('json', [user])
        return HttpResponse(data, content_type='application.json')

    except Exception:
        return HttpResponse ("User not found")

@csrf_exempt
def companyByID(request,company_ID):
    try:
        company = Company.objects.get(pk=company_ID)
        data = serializer.serialize('json', [company])
        return HttpResponse(data, content_type='application.json')

    except Exception:
        return HttpResponse("Company not found")