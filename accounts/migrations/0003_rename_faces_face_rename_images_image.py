# Generated by Django 4.1 on 2022-08-30 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Faces',
            new_name='Face',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]