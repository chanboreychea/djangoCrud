"""
URL configuration for Mydemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from MyApp import views
from MyApp.controllers import category_view, product_view

urlpatterns = [
    path("", views.homepage, name="/"),
    # category
    path("categories/index", category_view.index, name="categories-index"),
    path("categories/create", category_view.create),
    path("categories/store", category_view.store),
    path("categories/show/<id>", category_view.show, name="categories-show"),
    path("categories/edit/<id>", category_view.edit),
    path("categories/update/<id>", category_view.update),
    path("categories/destroy/<id>", category_view.destroy),
    path("categories/search", category_view.search),
    # product
    path("products/index", product_view.index, name="/products/index"),
    path("products/create", product_view.create),
    path("products/store", product_view.store),
    path("products/show/<id>", product_view.show, name="categories-show"),
    path("products/edit/<id>", product_view.edit),
    path("products/update/<int:id>", product_view.update),
    path("products/destroy/<int:id>", product_view.destroy),
    path("products/search", product_view.search),
]
