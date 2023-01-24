from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ListProductsViews.as_view(), name='list-products-views'),
    path('products/create/', views.CreateProductViews.as_view(), name='create-products-views'),
    path('products/<slug:slug>/', views.DetailProductViews.as_view(), name='detail-products-views'),

    path('categories/', views.ListCategoriesViews.as_view(), name='list-categories-views'),
    path('categories/create/', views.CreateCategoriesViews.as_view(), name='create-categories-views'),
    path('categories/<slug:slug>/', views.DetailCategoriesViews.as_view(), name='detail-categories-views'),

    path('categories/<slug:slug>/subcategories/', views.ListSubCategoriesViews.as_view(), name='list-subcategories-views'),
    path('categories/<slug:slug>/create/', views.CreateSubCategoriesViews.as_view(), name='create-subcategories-views'),
]