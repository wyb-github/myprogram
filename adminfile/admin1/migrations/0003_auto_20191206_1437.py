# Generated by Django 2.2.7 on 2019-12-06 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0002_categories_father'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryproperty',
            old_name='cid',
            new_name='category',
        ),
    ]
