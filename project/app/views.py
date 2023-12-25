

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
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
    paginate_by = 2

    
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
    fields = ('name', 'description', 'type', 'image', 'user')
    template_name = 'app/product_list.html'


class BasketView(generic.DetailView):
    model = Basket
    template_name = 'cabinet.html'
    context_object_name = 'basket'


def cabinet(request):
    return render(request, 'cabinet.html')


class Search(ListView):
    template_name = 'base.html'
    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] =self.request.GET.get