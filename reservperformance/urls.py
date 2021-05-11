from django.contrib import admin
from django.urls import path, include
from people_app import views as people_views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('accounts.urls')),

    path('', people_views.index, name='index'),
    path('peoplelist/', include('people_app.urls')),
    path('start_evaluation', people_views.start_evaluation, name='start_evaluation'),
    path('all_answers', people_views.all_results, name='all_results'),
    # path('evaluation', people_views.evaluation, name='evaluation'),
    path('', include('evaluation_app.urls'))
]
