from django.contrib import admin
from . models import Product, Category, SubCategory

admin.site.register([Product, Category, SubCategory])
