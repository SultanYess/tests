# Generated by Django 4.2.4 on 2023-08-31 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_owner_alter_pets_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
