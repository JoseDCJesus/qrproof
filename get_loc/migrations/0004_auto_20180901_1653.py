# Generated by Django 2.1 on 2018-09-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_loc', '0003_auto_20180901_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company_name',
            field=models.CharField(max_length=200),
        ),
    ]
