# Generated by Django 3.2.8 on 2021-10-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
