# Generated by Django 4.2.6 on 2024-02-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_imagetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtable',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='ImageTable',
        ),
    ]
