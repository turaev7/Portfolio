from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


class MeView(ListView):
    model = Me
    context_object_name="Info"
    template_name= "blog/service.html"
    
    
def index(request):
    model_1 = Me.objects.all()
    model_2 = Portfolio.objects.all()
    model_3 = Total.objects.all()
    model_4 = Blog.objects.all()
    contex = {
        'Info':model_1, 
        'Total':model_3,
        'Portfolio':model_2 ,
        "Blog":model_4
    }
    return render(request, 'blog/index.html', contex)

# class PortfolioView(ListView):
#     model = Me
#     context_object_name ="Service"
#     template_name = "blog/service.html"


# class TotalView(ListView):
#     model = Total
#     context_object_name ="Total"
#     template_name = "blog/total.html"


# class BlogView(ListView):
#     model = Total
#     context_object_name ="Total"
#     template_name = "blog/total.html"



# class TotalDetailView(DetailView):
#     model = Total
#     context_object_name ="total"
#     template_name = "blog/total.html"



# class TotalView(TemplateView):
#     template_name = "blog/total.html"
#     model = Total
#     context_object_name ="total"