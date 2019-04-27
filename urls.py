from django.urls import path

from . import views

urlpatterns = [
    path('registerUser', views.register_user, name='register_user'),
    path('validateLogin/<user_name>/<user_password>', views.login_validation, name='login_validation'),
    path('companyValidateLogin/<company_name>/<company_password>', views.companylogin_validation, name='companylogin_validation'),
<<<<<<< HEAD
    path('register_company', views.register_company, name='register_company')
    path('all_companys', views.get_companys, name='get_companys')

=======
    path('register_company', views.register_company, name='register_company'),
        path('all_users', views.get_users, name='get_users')
    path('user_info/<user_ID>', views.userByID, name='userByID'),
]
>>>>>>> 7d44aa29eafdfaea8f1693256c3e550c99f6636d
