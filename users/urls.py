from django.urls import path

from . import views

urlpatterns = [
    path('registerUser', views.register_user, name='register_user'),
    path('login_validation/<user_name>/<user_password>', views.validateLogin, name='validateLogin'),
    path('companyValidateLogin/<company_name>/<company_password>', views.companylogin_validation, name='companylogin_validation'),
    path('register_company', views.register_company, name='register_company'),
    path('all_users', views.get_users, name='get_users'),
    path('all_companys', views.get_companys, name='get_companys'),
    path('user_info/<user_ID>', views.userByID, name='userByID'),
    path('company_info/<company_ID>', views.companyByID, name='companyByID')
]
