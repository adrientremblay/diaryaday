# Generated by Django 2.2.1 on 2019-05-16 20:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_entry_essential'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='contents',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
