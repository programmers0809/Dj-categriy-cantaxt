# Generated by Django 4.2.1 on 2024-07-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'managed': True, 'verbose_name': 'foydalavchi', 'verbose_name_plural': 'ModelNames'},
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='number',
            field=models.IntegerField(default=99),
        ),
        migrations.AlterModelTable(
            name='usermodel',
            table='user',
        ),
    ]
