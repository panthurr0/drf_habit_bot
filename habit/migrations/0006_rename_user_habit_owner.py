# Generated by Django 5.0.6 on 2024-07-02 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0005_alter_habit_habit_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='user',
            new_name='owner',
        ),
    ]
