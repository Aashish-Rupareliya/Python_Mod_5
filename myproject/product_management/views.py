from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductMst, ProductSubCat

def add_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product = ProductMst(product_name=product_name)
        product.save()
        return redirect('add_product')
    return render(request, 'product_management/add_product.html')

def add_subcategory(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = get_object_or_404(ProductMst, pk=product_id)
        product_price = request.POST['product_price']
        product_image = request.FILES['product_image']
        product_model = request.POST['product_model']
        product_ram = request.POST['product_ram']
        subcat = ProductSubCat(product=product, product_price=product_price, product_image=product_image, product_model=product_model, product_ram=product_ram)
        subcat.save()
        return redirect('add_subcategory')
    products = ProductMst.objects.all()
    return render(request, 'product_management/add_subcategory.html', {'products': products})

def search_product(request):
    query = request.GET.get('q')
    if query:
        products = ProductMst.objects.filter(product_name__icontains=query)
    else:
        products = ProductMst.objects.all()
    return render(request, 'product_management/search_product.html', {'products': products})

def home(request):
    return render(request, 'product_management/home.html')


