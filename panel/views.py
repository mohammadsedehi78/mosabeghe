from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
import operator
from django.db.models import Q
from functools import reduce

from panel.forms import ProductForm
from panel.permissions import seller_required
from panel.models import Product


@login_required
def panel(request):
    return render(request, 'panel/panel.html')


@seller_required
@login_required
def new_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('panel')

    context = {
        'form': form
    }
    return render(request, 'panel/new_product.html', context=context)


@login_required
def become_seller(request):
    if request.user.is_seller:
        return render(request, 'panel/panel.html', context={'was_seller': True})
    else:
        request.user.is_seller = True
        request.user.save()
        return render(request, 'panel/panel.html', context={'was_seller': False})


@seller_required
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    assert product.user == request.user
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=product)
    return render(request, 'panel/edit_product.html', {'form': form})


@seller_required
@login_required
def products(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'panel/product.html', context={'products': products})


def all_products(request):
    from decimal import Decimal
    all_products = Product.objects.all()
    products = Product.objects.all()
    title = request.POST.get('title', "")
    min_price = request.POST.get('min_price', 0)
    max_price = request.POST.get('max_price', 0)

    if min_price == "":
        min_price = 0
    if max_price == "":
        max_price = 0

    title = title.strip()

    products = all_products.filter(
        Q(price__gte=min_price) | Q(
            price__lte=max_price) | Q(name__contains=title)
    )

    return render(request, 'panel/all_products.html', context={'products': products.distinct()})


def rate(request):
    rate = request.POST.get('rate')
    rate = int(rate)
    name = request.POST.get('name')
    products = Product.objects.filter(name=name).first()

    products.countrate = products.countrate+1
    products.sumrate += rate
    products.rate = products.sumrate/products.countrate

    products.save()
    all_products = Product.objects.all()

    return render(request, 'panel/all_products.html', context={'products': all_products})
