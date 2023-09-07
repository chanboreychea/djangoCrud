from django.shortcuts import render

# Create your views here.
# from MyApp.models import Product


def homepage(request):
    return render(request, 'index.html')


# def getProductById(request,id):
#     return render(request,'product.html',{'id':id})
#
# def getAllProducts(request):
#     data=[]
#
#     product = Product()
#     product.id = 1
#     product.name = 'coca'
#     product.qty = 100
#     product.price = 1.9
#     data.append(product)
#
#     product = Product()
#     product.id = 2
#     product.name = 'pepsi'
#     product.qty = 200
#     product.price = 2.9
#     data.append(product)
#
#     product = Product()
#     product.id = 3
#     product.name = 'sting'
#     product.qty = 300
#     product.price = 3.9
#     data.append(product)
#
#     return render(request,'product.html',{'products':data})