# Generated by Django 4.2.2 on 2023-06-26 09:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('end', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('label', models.TextField()),
                ('text', models.TextField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.document')),
            ],
        ),
    ]
