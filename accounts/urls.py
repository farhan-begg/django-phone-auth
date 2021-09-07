from django.urls import path
from accounts.views import register, login_view

urlpatterns=[
    path('register/', register, name="register"),
    path('login/', login_view, name="login")
]