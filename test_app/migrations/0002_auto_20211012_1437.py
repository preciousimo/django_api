# Generated by Django 3.2.8 on 2021-10-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='is_live',
            new_name='is_alive',
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
