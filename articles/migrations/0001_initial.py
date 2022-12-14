# Generated by Django 4.1.1 on 2022-11-05 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture', models.ImageField(blank=True, upload_to='C:\\Users\\User\\Desktop\\Python_projects\\pharmacy_site_1\\pharmacy_site\\media\\article_pics')),
            ],
        ),
    ]
