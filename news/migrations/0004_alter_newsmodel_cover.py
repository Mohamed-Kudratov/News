# Generated by Django 3.2.4 on 2021-06-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
