# Generated by Django 3.1.5 on 2021-05-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customaccount',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='customemail',
            field=models.EmailField(default='', max_length=60, null=True),
        ),
    ]
