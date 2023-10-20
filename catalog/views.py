from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

from catalog.forms import ProductForm


class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/testmain.html'


# def index(request):
#     return render(request, 'catalog/testmain.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f"{name} ({email})")

    context = {
        'title':'Контакты'
        }


    return render(request, 'catalog/testsecond_contacts.html', context)


class MerchandiseListView(ListView):
    model = Product
    template_name = 'catalog/merchandise.html'


# def merchandise(request):
#     product_list = Product.objects.all()
#
#     context = {
#         'object_list':product_list
#     }
#
#     return render(request, 'catalog/merchandise.html', context)



class ProductDetailView(DetailView):
    model = Product
    # template_name = "catalog/view_product.html" - view_product


# def view_product(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product_item,
#     }
#     return render(request, "catalog/view_product.html", context)


# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('title', 'description', 'preview', 'category', 'purchase_price', 'date_creation', 'date_modified')
#     success_url = reverse_lazy('catalog:merchandise')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:merchandise')


# class ProductUpdateView(UpdateView):
#     model = Product
#     fields = ('title', 'description', 'preview', 'category', 'purchase_price', 'date_creation', 'date_modified')
#     success_url = reverse_lazy('catalog:merchandise')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:merchandise')



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:merchandise')



def toggle_activity(request, pk):
    product_item = get_object_or_404(Product,pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True
    product_item.save()

    return redirect(reverse('catalog:merchandise'))

