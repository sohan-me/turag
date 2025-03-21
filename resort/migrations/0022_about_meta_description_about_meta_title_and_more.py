# Generated by Django 4.2.19 on 2025-03-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resort', '0021_alter_plan_extra_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='amenities',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='amenities',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='due_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='paid_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='complementary',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complementary',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='venueinfo',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venueinfo',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='venueinfo',
            name='content',
            field=models.TextField(),
        ),
    ]
