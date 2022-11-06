import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from products import models
import decimal
from pharmacy_site import settings

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product
    title = factory.Sequence(lambda n: "product_title_fuflomizin_%d" %n)
    description = fake.sentence()
    pure_price = fake.random_int(min=5, max=200)
    discount_percent = fake.random_int(min=0, max=99)
    discounted_price = 0
    picture = settings.MEDIA_ROOT + "\\product_pics\\test.png"
    number_in_stock = fake.random_int()
    category = 'eye_glasses'
    brand = 'brand_1'

    @factory.lazy_attribute
    def discounted_price(self):
        return (decimal.Decimal(self.pure_price) - decimal.Decimal(self.pure_price)*decimal.Decimal((decimal.Decimal(self.discount_percent)/100)))

register(ProductFactory)
