# Generated by Django 2.1.7 on 2019-02-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, max_length=30)),
                ('room_number', models.IntegerField(blank=True, null=True)),
                ('nobeds', models.IntegerField(blank=True, null=True)),
                ('room_type', models.PositiveSmallIntegerField(choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple')])),
            ],
        ),
    ]
