# Generated by Django 4.2.4 on 2023-08-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_delete_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('surname', models.CharField(max_length=55)),
                ('number', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pets',
            name='photo',
            field=models.ImageField(blank=True, upload_to='sultan/static/photo/'),
        ),
    ]