# Generated by Django 5.1.1 on 2024-11-05 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_subsection_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название подраздела')),
                ('content', models.FileField(upload_to='uploads/', verbose_name='Содержание')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('subsection', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.subsection')),
            ],
            options={
                'verbose_name': 'Файлы',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
