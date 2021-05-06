from django.contrib import admin
from django.urls import path, include
from people_app import views as people_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # redirect to my particular app
    path('', people_views.index, name='index'),
    path('peoplelist/', include('people_app.urls')),
    path('contact', people_views.contact, name='contact'),
    path('about-us', people_views.about, name='about'),
    path('account/', include('users_app.urls')),
]
