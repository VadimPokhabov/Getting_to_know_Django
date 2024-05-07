from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, HomePageView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomePageView.as_view()),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
]
