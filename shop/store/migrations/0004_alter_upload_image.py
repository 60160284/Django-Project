# Generated by Django 3.2 on 2021-05-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210506_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/product/'),
        ),
    ]