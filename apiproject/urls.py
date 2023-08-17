"""apiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from apiapp import views
from rest_framework.authtoken.views import obtain_auth_token
# import requests

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('user/register',views.register.as_view(),name='register'),
    path('user/login/',obtain_auth_token,name="login"),
]

# old_url = "http://:8000/user/register"

# new_url = "https://api.learnyn.in/user/register"

# response = requests.get(new_url)

# print(response.text)



# base_url = "https://api.learnyn.in"
# login_endpoint = "/user/login/"

# url = base_url + login_endpoint

# data = {
#     "username": "archana"
#     "password": "achu1234"
# }

# response = requests.post(url, json=data)

# if response.status_code == 200:
#     print("login successfully!")
#     print("Response:", response.json())
# else:
#     print("login failed.")
#     print("Status Code:", response.status_code)
#     print("Response:", response.text)