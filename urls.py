from django.urls import path

from . import views

urlpatterns = [
    path('registerUser', views.register_user, name='register_user'),
    path('validateLogin/<user_name>/<user_password>', views.login_validation, name='login_validation')

]