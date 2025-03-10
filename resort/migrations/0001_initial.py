# Generated by Django 4.2.19 on 2025-03-04 06:36

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=260)),
                ('slogan', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('Restaurant', 'Restaurant'), ('Event', 'Event'), ('Recreation', 'Recreation'), ('Play Ground', 'Play Ground'), ('Kids Zone', 'Kids Zone'), ('Hall', 'Hall'), ('Outdoor', 'Outdoor')], max_length=20)),
                ('venue', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Gazipur', 'Gazipur')], max_length=20)),
                ('tags', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='room/amenities/')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=160)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/')),
                ('alt_text', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Complementary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='room/amenities/')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'complementaries',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=55)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(blank=True, max_length=300, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('mark_as_read', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('Outdoor', 'Outdoor'), ('Dining', 'Dining'), ('Activities', 'Activities'), ('Events', 'Events'), ('Interior', 'Interior'), ('Rooms', 'Rooms')], max_length=20)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('alt_text', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('description', models.TextField()),
                ('dynamic_image', models.ImageField(blank=True, null=True, upload_to='room/dynamic_image/')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('Cottage', 'Cottage'), ('Suite', 'Suite'), ('Villa', 'Villa'), ('Duplex', 'Duplex'), ('Lake View', 'Lake View'), ('River View', 'River View'), ('Deluxe', 'Deluxe')], max_length=20)),
                ('venue', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Gazipur', 'Gazipur')], max_length=20)),
                ('tags', models.CharField(max_length=300)),
                ('is_available', models.BooleanField(default=True)),
                ('amenities', models.ManyToManyField(blank=True, related_name='room', to='resort.amenities')),
                ('complementary', models.ManyToManyField(blank=True, related_name='room', to='resort.complementary')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facebook', models.URLField(blank=True, max_length=300, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=300, null=True)),
                ('instagram', models.URLField(blank=True, max_length=300, null=True)),
                ('youtube', models.URLField(blank=True, max_length=300, null=True)),
                ('tiktok', models.URLField(blank=True, max_length=300, null=True)),
                ('pinterest', models.URLField(blank=True, max_length=300, null=True)),
                ('whatsapp', models.URLField(blank=True, max_length=300, null=True)),
                ('twitter', models.URLField(blank=True, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomImageLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room/images/')),
                ('alt_text', models.CharField(blank=True, max_length=100, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_image', to='resort.room')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('adults', models.PositiveIntegerField()),
                ('children', models.PositiveIntegerField()),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=100)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resort.room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActivityImageLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='activity/images/')),
                ('alt_text', models.CharField(blank=True, max_length=100, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_image', to='resort.activity')),
            ],
        ),
    ]
