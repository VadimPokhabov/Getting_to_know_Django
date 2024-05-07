from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product
from catalog.user_cases import save_feedback


class HomePageView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            save_feedback(
                name=request.POST.get('name'),
                phone=request.POST.get('phone'),
                message=request.POST.get('message')
            )
        return HttpResponseRedirect(reverse('catalog:contacts'))


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
