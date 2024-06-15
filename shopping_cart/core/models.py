from django.db import models

# Create your models here.
# CATEGORY_CHOICES = (
#     ('EC','Electronics'),
#     ('CG', 'Clothing'),
#     ('AC', 'Accessories')
# )


class Item(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name

class ItemImage(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images',name='item_image')
    thumbnail = models.ImageField(upload_to="thumbnails",null=True)


class ItemTag(models.Model):
    items = models.ManyToManyField(Item,blank=True)

    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    category = models.ManyToManyField(ItemTag)
    name = models.CharField(max_length=120,default='Clothing')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

class Order(models.Model):
    pass
