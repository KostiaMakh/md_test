# Generated by Django 4.0.6 on 2022-08-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_alter_vehicle_office'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ('pk',)},
        ),
    ]