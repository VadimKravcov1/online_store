from django.urls import path
from catalog.views import index, contacts, merchandise

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', index, name = 'index'),
    path('contacts', contacts, name = 'contacts'),
    path('merchandise', merchandise, name = 'merchandise')
]