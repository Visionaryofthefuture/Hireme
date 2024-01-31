# Generated by Django 4.2.9 on 2024-01-31 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hireme', '0003_alter_user_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='resume',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Hireme.user')),
                ('resume', models.FileField(default=None, upload_to='media/')),
            ],
            bases=('Hireme.user',),
        ),
    ]
