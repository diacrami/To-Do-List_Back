# Generated by Django 5.0.3 on 2024-03-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_tasks_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='isActive',
            field=models.CharField(default='T', max_length=1),
        ),
    ]
