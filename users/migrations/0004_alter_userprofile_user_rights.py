# Generated by Django 4.1.1 on 2022-11-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_user_rights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_rights',
            field=models.CharField(choices=[('user', 'User'), ('employee', 'Employee'), ('admin', 'Admin')], default='user', max_length=20),
        ),
    ]
