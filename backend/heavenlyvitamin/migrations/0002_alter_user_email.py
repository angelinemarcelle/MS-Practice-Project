# Generated by Django 3.2.25 on 2025-06-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heavenlyvitamin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
