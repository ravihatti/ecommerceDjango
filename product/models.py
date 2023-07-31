from typing import Iterable, Optional
from django.db import models

# Create your models here.
from base.models import BaseModel
from django.utils.text import slugify


class ColorVariant(BaseModel):
    color_name = models.CharField(max_length= 225)
    price = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.color_name
class SizeVariant(BaseModel):
    size_name = models.CharField(max_length= 225)
    price = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.size_name

class Category(BaseModel):
    category_name = models.CharField(max_length=500)
    category_image = models.ImageField(upload_to="categories")
    slug = models.SlugField(unique=True,null= True,blank=True)
    def save(self,*args,**kargws):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kargws)
    def __str__(self) -> str:
        return self.category_name
class Product(BaseModel):
    product_name = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price = models.IntegerField()
    product_description = models.TextField(max_length=500)
    slug = models.SlugField(unique=True,null= True,blank=True)
    color_varient = models.ManyToManyField(ColorVariant,blank=True)
    size_varient = models.ManyToManyField(SizeVariant,blank=True)
    def save(self,*args,**kargws):
        self.slug = slugify(self.product_name)
        super(Product,self).save(*args,**kargws)
    def __str__(self) -> str:
        return self.product_name 
class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload_to="product")