from django.urls import path
from catalog.views import contacts, merchandise, ProductListView, ProductDetailView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name = 'index'),
    path('contacts', contacts, name = 'contacts'),
    path('merchandise', merchandise, name = 'merchandise'),
    path('<int:pk>/view/', ProductDetailView.as_view(), name = 'view_product')
]