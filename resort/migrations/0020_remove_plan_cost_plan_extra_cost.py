# Generated by Django 4.2.19 on 2025-03-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resort', '0019_remove_plan_is_full_board_alter_plan_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='cost',
        ),
        migrations.AddField(
            model_name='plan',
            name='extra_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
