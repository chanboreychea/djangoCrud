from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.views.decorators.http import require_GET, require_POST
from MyApp.models import Category


@require_GET
def index(request):
    category = Category.objects.all().order_by("id").reverse()
    context = {"categories": category}
    return render(request, "categories/index.html", context)


@require_POST
def search(request):
    categories = Category.objects.filter(
        name__contains=request.POST["txtSearch"]
    ).values()
    context = {"categories": categories}
    return render(request, "categories/index.html", context)


@require_GET
def create(request):
    return render(request, "categories/create.html")


@require_POST
def store(request):
    category = Category()
    category.name = request.POST["txtCategoryName"]
    category.createBy = "1"
    category.updateBy = "1"
    category.save()
    return redirect("/categories/create")


def show(request, id):
    category = Category.objects.get(id=id)
    context = {"category": category}
    return render(request, "categories/show.html", context)


def edit(request, id):
    category = Category.objects.get(id=id)
    context = {"category": category}
    return render(request, "categories/edit.html", context)


@require_POST
def update(request, id):
    category = Category.objects.get(id=id)
    category.name = request.POST["txtCategoryName"]
    category.createBy = "2"
    category.updateBy = "2"
    category.save()
    return redirect("/categories/index")


@require_GET
def destroy(request, id):
    category = Category.objects.get(id=id).delete()
    return redirect("/categories/index")
