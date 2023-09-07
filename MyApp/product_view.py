from django.shortcuts import render

# Create your views here.
from MyApp.models import Product
from django.views.decorators.http import require_GET, require_POST


@require_GET
def index(request):

    return render(request, "products/index.html")
