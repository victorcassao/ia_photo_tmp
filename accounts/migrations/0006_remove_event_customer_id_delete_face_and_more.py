# Generated by Django 4.1 on 2022-08-31 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='customer_id',
        ),
        migrations.DeleteModel(
            name='Face',
        ),
        migrations.RemoveField(
            model_name='image',
            name='event_id',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
