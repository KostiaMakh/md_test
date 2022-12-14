# Generated by Django 4.0.6 on 2022-07-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='office',
            name='country',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='office',
            name='region',
            field=models.CharField(max_length=256),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
