# Generated by Django 5.0.6 on 2024-07-03 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0010_reportcard'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student', 'date_generated')},
        ),
    ]