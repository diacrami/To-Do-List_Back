# Generated by Django 4.2.3 on 2024-03-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_tasks_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='createdAt',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='updatedAt',
            field=models.DateField(auto_now=True),
        ),
    ]
