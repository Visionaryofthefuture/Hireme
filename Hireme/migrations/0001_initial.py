# Generated by Django 5.0.1 on 2024-01-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=254)),
                ('resume', models.FileField(default='', upload_to='media')),
            ],
        ),
    ]
