# Generated by Django 3.0.4 on 2020-03-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('gst_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]
