# Generated by Django 5.0.6 on 2024-07-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0011_alter_reportcard_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_generated',
            field=models.DateField(auto_now_add=True),
        ),
    ]
