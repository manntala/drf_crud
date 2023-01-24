from products.models import Product, Category, SubCategory
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class ViewProducts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/index.html'

    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()

        context = {
            'products': products,
            'categories': categories,
            'subcategories': subcategories,

        }
        return Response(context)
