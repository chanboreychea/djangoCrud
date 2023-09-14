import os
from django.shortcuts import redirect, render

# Create your views here.
from MyApp.models import Category, Product
from django.views.decorators.http import require_GET, require_POST


@require_GET
def index(request):
    products = Product.objects.all().order_by("id")
    context = {"products": products}
    return render(request, "products/index.html", context)


@require_POST
def search(request):
    products = Product.objects.filter(name__contains=request.POST["txtSearch"]).values()
    context = {"products": products}
    return render(request, "products/index.html", context)


@require_GET
def create(request):
    categories = Category.objects.all().order_by("id")
    context = {"categories": categories}
    return render(request, "products/create.html", context)


@require_POST
def store(request):
    product = Product()
    product.barcode = request.POST["txtBarcode"]
    product.name = request.POST["txtProductName"]
    product.unitPrice = request.POST["txtPrice"]
    product.qtyInstock = request.POST["txtQuantity"]
    product.createBy = "1"
    product.updateBy = "1"
    if len(request.FILES) != 0:
        product.photo = request.FILES["photo"]
    product.category_id = request.POST["optCategory"]

    product.save()
    return redirect("/products/create")


def show(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.get(id=product.category_id)
    context = {"product": product, "category": category}
    return render(request, "products/show.html", context)


def edit(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all().order_by("id")
    context = {"product": product, "categories": categories}
    return render(request, "products/edit.html", context)


@require_POST
def update(request, id):
    product = Product.objects.get(id=id)
    product.barcode = request.POST["txtBarcode"]
    product.name = request.POST["txtProductName"]
    product.unitPrice = request.POST["txtPrice"]
    product.qtyInstock = request.POST["txtQuantity"]
    product.createBy = "1"
    product.updateBy = "1"

    if len(request.FILES) != 0:
        product.photo = request.FILES["photo"]

    product.category_id = request.POST["optCategory"]
    product.save()

    return redirect("/products/index")


@require_GET
def destroy(request, id):
    product = Product.objects.get(id=id).delete()
    return redirect("/products/index")
