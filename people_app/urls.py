from django.urls import path
from people_app import views  # import the view

urlpatterns = [
    # set the name for the view and for the link
    path('', views.people, name='peoplelist'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
