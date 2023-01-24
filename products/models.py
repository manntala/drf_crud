from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
