# Generated by Django 5.0.6 on 2024-07-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_alter_habit_is_nice_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit_time',
            field=models.TimeField(auto_now_add=True, help_text='Время привычки', null=True),
        ),
    ]
