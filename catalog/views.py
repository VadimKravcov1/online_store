from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView




class ProductListView(ListView):
    model = Product
    template_name = 'catalog/testmain.html'


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


def merchandise(request):
    product_list = Product.objects.all()

    context = {
        'object_list':product_list
    }

    return render(request, 'catalog/merchandise.html', context)



class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/view_product.html"


# def view_product(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product_item,
#     }
#     return render(request, "catalog/view_product.html", context)





