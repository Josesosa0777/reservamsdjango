from django.urls import path
from people_app import views  # import the view

urlpatterns = [
    # set the name for the view and for the link
    path('', views.people, name='peoplelist'),
    path('contact', views.contact, name='contact'),
    path('evaluation', views.evaluation, name='evaluation'),
    path('about', views.about, name='about'),
    path('delete/<people_id>', views.delete_people, name='delete_people'),
    path('edit/<people_id>', views.edit_people, name='edit_people'),
]
