from django.urls import path
from . import views

urlpatterns=[
    path('',views.get_home.as_view(),name='home'),
    path('about',views.get_about.as_view(),name='about'),
]