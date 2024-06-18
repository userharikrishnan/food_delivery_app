# Generated by Django 5.0.3 on 2024-06-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0008_menu_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurantName', models.CharField(default='', max_length=50)),
                ('Image_url', models.URLField(default='https://placehold.co/200x250')),
                ('name', models.CharField(max_length=100)),
                ('count', models.DecimalField(decimal_places=0, max_digits=10)),
                ('sumTotal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]