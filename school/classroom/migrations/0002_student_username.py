# Generated by Django 3.0.5 on 2020-04-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
