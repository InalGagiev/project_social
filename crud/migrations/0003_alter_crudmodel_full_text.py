# Generated by Django 4.1.4 on 2023-04-11 14:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_remove_crudmodel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudmodel',
            name='full_text',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
