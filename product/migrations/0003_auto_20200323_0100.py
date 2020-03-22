# Generated by Django 3.0.4 on 2020-03-22 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('product', '0002_productmodel_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyModel'),
        ),
    ]
