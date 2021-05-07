from django.urls import path
from evaluation_app import views  # import the view

urlpatterns = [
    # set the name for the view and for the link
    path('evaluate', views.evaluation, name='evaluate'),
]
