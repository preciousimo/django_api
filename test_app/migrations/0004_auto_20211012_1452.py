# Generated by Django 3.2.8 on 2021-10-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20211012_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
