# Generated by Django 3.2.8 on 2021-10-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_award_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='linktosite',
            field=models.URLField(default=None, null=True),
        ),
    ]