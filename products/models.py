from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import decimal
import os
from PIL import Image

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
product_image_dir = base_dir + '\media\product_pics'

product_categories = (
    ('flu', 'Flu medicine'),
    ('eye_glasses', 'Eye glasses'),
    ('eye_medicine', 'Eye medicine'),
    ('heart', 'Heart medicine'),
)

brands = (
    ('choose_brand', ''),
    ('brand_1', 'Brand 1'),
    ('brand_2', 'Brand 2'),
    ('brand_3', 'Brand 3'),
    ('brand_4', 'Brand 4'),
    ('brand_5', 'Brand 5'),
)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percent = models.IntegerField(default=0, validators=PERCENTAGE_VALIDATOR, blank=True)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    picture = models.ImageField(blank=True, upload_to=product_image_dir)
    number_in_stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=product_categories, default='flu')
    brand = models.CharField(max_length=100, choices=brands, default='choose_brand')
    

    @property
    def get_price_with_discount(self):
        return decimal.Decimal(self.price) - decimal.Decimal(self.price)*decimal.Decimal((decimal.Decimal(self.discount_percent)/100))

    def save(self, *args, **kwargs):
        self.discounted_price = self.get_price_with_discount
        super(Product, self).save(*args, **kwargs)
        try:
            img = Image.open(self.picture.path)

            if img.height > 200 or img.width > 320:
                output_size = (320, 200)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        except ValueError:
            pass

    def __str__(self):
        return f'{self.title}'