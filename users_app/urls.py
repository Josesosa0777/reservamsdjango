from django.urls import path
from users_app import views

urlpatterns = [
    # set the name for the view and for the link:
    path('register', views.register, name='register'),
]
