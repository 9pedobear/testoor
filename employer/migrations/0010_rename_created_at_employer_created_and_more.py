# Generated by Django 4.0.3 on 2022-03-25 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0009_employer_created_at_employer_is_published_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='employer',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
