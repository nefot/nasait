# Generated by Django 5.1.1 on 2024-11-04 16:47

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_subsection_section_delete_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('subsection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.subsection')),
            ],
            options={
                'verbose_name': 'Нормативно правовая база',
                'verbose_name_plural': 'Нормативно правовая база',
            },
            bases=('core.subsection',),
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('subsection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.subsection')),
            ],
            options={
                'verbose_name': 'Справочные материалы',
                'verbose_name_plural': 'Справочные материалы',
            },
            bases=('core.subsection',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('subsection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.subsection')),
            ],
            options={
                'verbose_name': 'Организации',
                'verbose_name_plural': 'Организации',
            },
            bases=('core.subsection',),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterModelOptions(
            name='subsection',
            options={'verbose_name': 'Специалистам', 'verbose_name_plural': 'Специалистам'},
        ),
        migrations.AlterField(
            model_name='subsection',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=500, verbose_name='Содержание'),
        ),
    ]
