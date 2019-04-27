from django.urls import path

from . import views

urlpatterns = [
    path('registerUser', views.register_user, name='register_user'),
    path('validateLogin/<user_name>/<user_password>', views.login_validation, name='login_validation'),
    path('companyValidateLogin/<company_name>/<company_password>', views.companylogin_validation, name='companylogin_validation'),
    path('register_company', views.register_company, name='register_company'),
    path('all_users', views.get_users, name='get_users'),
    path('user_info/<user_ID>', views.userByID, name='userByID'),
      path('company_info/<company_ID>', views.companyByID, name='companyByID')
]
