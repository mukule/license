# Generated by Django 4.2.2 on 2023-06-21 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_license_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='license',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.licensecategory'),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='license',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='license',
            name='weblink',
            field=models.URLField(blank=True),
        ),
    ]
