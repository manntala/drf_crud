from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview' ),
    path('products/', views.productList, name='products' ),
    path('product/detail/<slug>/', views.productDetail, name='product-detail' ),
    path('product/create/', views.productCreate, name='product-create' ),
    path('product/edit/<slug>/', views.productUpdate, name='product-edit' ),
    path('product/delete/<slug>/', views.productDelete, name='product-delete' ),

    path('categories/', views.categoryList, name='categories' ),
    path('category/detail/<slug>/', views.categoryDetail, name='category-detail' ),
    path('category/create/', views.categoryCreate, name='category-create' ),
    path('category/edit/<slug>/', views.categoryUpdate, name='category-edit' ),
    path('category/delete/<slug>/', views.categoryDelete, name='category-delete' ),

    path('category/<slug>/', views.subCategoryList, name='subcategories' ),
    path('category/<slug>/create/', views.subCategoryCreate, name='subcategory-create' ),

    path('cbv/', views.ApiListView.as_view(), name='api-list-view')
]