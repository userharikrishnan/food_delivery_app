# Generated by Django 5.0.3 on 2024-06-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='profile_images/default.jpg', upload_to='profile_images/'),
        ),
    ]
