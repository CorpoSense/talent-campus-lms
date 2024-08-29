# Generated by Django 5.0.7 on 2024-08-29 14:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorieName', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, related_name='instructor', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('rating', models.FloatField(default=1.0)),
                ('status', models.IntegerField(choices=[('draft', 0), ('published', 1), ('expired', 2)], default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='courses', to='api.coursecategorie')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='api.instructor')),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
    ]
