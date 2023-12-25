

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *

class ProductCreate(LoginRequiredMixin,CreateView):
    model = Product
    fields = ('name', 'description', 'type', 'image')
    template_name = 'product_create.html'
    success_url = reverse_lazy('base')


class ProductList(generic.ListView):
    model = Product
    fields = ('name', 'description', 'type', 'image', 'date', )
    template_name = 'base.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.order_by('-date')[:5]
    
class RegistrationUserForm(CreateView):
    form_class = RegistrateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProductListMax(generic.ListView):
    model = Product
    fields = ('name', 'description', 'type', 'image', 'id')
    template_name = 'product_max.html'
    context_object_name = 'product'

class ProductView(generic.DetailView):
    model = Product
    fields = ('name', 'description', 'type', 'image')
    template_name = 'app/product_list.html'

class BasketView(generic.DetailView):
    model = Basket
    template_name = 'cabinet.html'


def cabinet(request):
    return render(request, 'cabinet.html')