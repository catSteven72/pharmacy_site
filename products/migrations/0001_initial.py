# Generated by Django 4.1.1 on 2022-11-05 23:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_percent', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('picture', models.ImageField(blank=True, upload_to='C:\\Users\\User\\Desktop\\Python_projects\\pharmacy_site_1\\pharmacy_site\\media\\product_pics')),
                ('number_in_stock', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('flu', 'Flu medicine'), ('eye_glasses', 'Eye glasses'), ('eye_medicine', 'Eye medicine'), ('heart', 'Heart medicine')], default='flu', max_length=100)),
                ('brand', models.CharField(choices=[('choose_brand', ''), ('brand_1', 'Brand 1'), ('brand_2', 'Brand 2'), ('brand_3', 'Brand 3'), ('brand_4', 'Brand 4'), ('brand_5', 'Brand 5')], default='choose_brand', max_length=100)),
            ],
        ),
    ]
