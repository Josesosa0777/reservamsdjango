from django.contrib import admin
from django.urls import path, include
from people_app import views as people_views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('accounts.urls')),

    path('', people_views.index, name='index'),
    path('peoplelist/', include('people_app.urls')),
    path('contact', people_views.contact, name='contact'),
    path('about-us', people_views.about, name='about'),
    # path('evaluation', people_views.evaluation, name='evaluation'),
    path('', include('evaluation_app.urls'))
]
