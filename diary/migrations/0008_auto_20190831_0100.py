# Generated by Django 2.2.4 on 2019-08-31 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_auto_20190520_0732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='writer',
            options={},
        ),
        migrations.AlterModelManagers(
            name='writer',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='writer',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='writer',
            name='name',
            field=models.CharField(default='default name', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='writer',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]