from django.shortcuts import render
from .models import User,Course,Batch,Role,Feedback,TimeTable,Trainer,Placement,ClassRoom,Hr
from django.views.generic import TemplateView
from django.views import generic

# Create your views here.

class get_home(TemplateView):
    model=User
    template_name = 'adminapp/index.html'


class get_about(TemplateView):
    model=User
    template_name = 'adminapp/about-us.html'



