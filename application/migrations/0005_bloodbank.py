# Generated by Django 3.2.13 on 2022-06-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_bloodrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodbank',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('no', models.CharField(max_length=100)),
                ('h_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('blood_type', models.CharField(max_length=100)),
                ('av_or_not', models.CharField(max_length=100)),
            ],
        ),
    ]
