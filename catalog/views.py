from django.shortcuts import render
from catalog.models import Product


def index(request):
    return render(request, 'catalog/testmain.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f"{name} ({email})")


    return render(request, 'catalog/testsecond_contacts.html')


def merchandise(request):
    product_list = Product.objects.all()

    context = {
        'object_list':product_list
    }

    return render(request, 'catalog/merchandise.html', context)









