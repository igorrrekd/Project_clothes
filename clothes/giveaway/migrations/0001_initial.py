# Generated by Django 3.2.9 on 2021-11-08 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna')], default=1)),
                ('categories', models.ManyToManyField(to='giveaway.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('phone_number', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=5)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pic_up_comment', models.TextField(blank=True, null=True)),
                ('categories', models.ManyToManyField(to='giveaway.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.institution')),
            ],
        ),
    ]
