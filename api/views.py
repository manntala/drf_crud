from django.shortcuts import render
from django.http import JsonResponse

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import ProductSerializer, CategorySerializer, SubCategorySerializer

from products.models import Product, Category, SubCategory

@api_view(['GET'])
def apiOverview(request):
    #/products -> GET: list all products, paginated
    #/products/create/ ->POST: create new product
    #/products/<slug> -> GET, PATCH, PUT, DELETE: view, edit and delete product

    api_urls = {
        'GET': '/products/',
        'POST': '/products/create',
        'GET, PATCH, PUT, DELETE': '/products/<slug>',
    }
    return Response(api_urls)


@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def productDetail(request, slug):
    products = Product.objects.get(slug=slug)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def productUpdate(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, slug):
    product = Product.objects.get(slug=slug)
    product.delete()

    return Response("Successfully Deleted!")


# Categories
# /categories -> GET: list all products, paginated
# /categories/create/ -> POST: create new category
# /categories/<slug> -> GET, PATCH, PUT, DELETE: view, edit and delete category

@api_view(['GET'])
def categoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categoryDetail(request, slug):
    categories =  Category.objects.get(slug=slug)
    serializer =  CategorySerializer(categories, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def categoryCreate(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def categoryUpdate(request, slug):
    category = Category.objects.get(slug=slug)
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def categoryDelete(request, slug):
    category = Category.objects.get(slug=slug)
    category.delete()

    return Response("Successfully Deleted!")


# SubCategory
@api_view(['GET'])
def subCategoryList(request, slug):
    category = Category.objects.get(slug=slug)
    # subcategory = SubCategory.objects.get(category=slug)
    subcategory = category.subcategory_set.all()
    serializer = SubCategorySerializer(subcategory, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def subCategoryCreate(request):
    serializer = SubCategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)