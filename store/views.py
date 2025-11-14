from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import CategoryForm, ProductForm

def home(request):
    return render(request, 'store/home.html')

# CATEGORIES
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'store/categories_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:categories_list')
    else:
        form = CategoryForm()
    return render(request, 'store/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('store:categories_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'store/category_form.html', {'form': form})

# PRODUCTS
def products_list(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'store/products_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store:products_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('store:products_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form})

# CREDITS & CONTACT
def credits(request):
    return render(request, 'store/credits.html')

def contact(request):
    return render(request, 'store/contact.html')
