# Generated by Django 4.1.4 on 2023-04-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Аккаунты', 'verbose_name_plural': 'Аккаунты'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
