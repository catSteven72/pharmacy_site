import pytest
from products import models
import decimal
from pharmacy_site import settings

pic = settings.MEDIA_ROOT + "\\product_pics\\test.png"

def test_db_product_insert_data(db, product_factory):
    new_product = product_factory.create(
        title='fuflomizin_xx',
        description='lorem10', 
        price=20,
        discount_percent=20, 
        picture=pic, 
        number_in_stock=15, 
        category='flu',
        brand='brand_2'
        )

    assert new_product.title == 'fuflomizin_xx'
    assert new_product.description == 'lorem10'
    assert new_product.price == 20
    assert new_product.discount_percent == 20
    assert new_product.discounted_price == 16
    assert new_product.picture == pic
    assert new_product.number_in_stock == 15
    assert new_product.category == 'flu'
    assert new_product.brand == 'brand_2'