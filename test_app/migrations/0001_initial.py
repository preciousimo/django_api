# Generated by Django 3.2.8 on 2021-10-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('phone', models.PositiveIntegerField()),
                ('is_live', models.BooleanField(default=False)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
