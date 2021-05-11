from django.urls import path
from people_app import views  # import the view

urlpatterns = [
    # set the name for the view and for the link
    path('peoplelist', views.people, name='peoplelist'),
    path('start_evaluation', views.start_evaluation, name='start_evaluation'),
    path('evaluation', views.evaluation, name='evaluation'),
    path('all_results', views.all_results, name='all_results'),
    path('delete/<people_id>', views.delete_people, name='delete_people'),
    path('edit/<people_id>', views.edit_people, name='edit_people'),
    path('evaluated_people', views.evaluated_people, name='evaluated_people'),
]
