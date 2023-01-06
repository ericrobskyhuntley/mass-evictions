# Generated by Django 4.1.5 on 2023-01-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attorneys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.TextField(blank=True, null=True, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('add1', models.TextField(blank=True, null=True)),
                ('add2', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('zip', models.TextField(blank=True, null=True)),
                ('office', models.TextField(blank=True, null=True)),
                ('add_p', models.TextField(blank=True, null=True)),
                ('match_type', models.TextField(blank=True, null=True)),
                ('geocoder', models.TextField(blank=True, null=True)),
                ('geometry', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attorneys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Defendants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('docket', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'defendants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Docket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('docket', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'docket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('session', models.TextField(blank=True, null=True)),
                ('locality', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('docket', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Filings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('zip', models.TextField(blank=True, null=True)),
                ('case_type', models.TextField(blank=True, null=True)),
                ('file_date', models.DateField(blank=True, null=True)),
                ('case_status', models.TextField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('ptf_bar', models.TextField(blank=True, null=True)),
                ('def_bar', models.TextField(blank=True, null=True)),
                ('dispo', models.TextField(blank=True, null=True)),
                ('dispo_date', models.DateField(blank=True, null=True)),
                ('docket', models.TextField(blank=True, null=True, unique=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('add1', models.TextField(blank=True, null=True)),
                ('add2', models.TextField(blank=True, null=True)),
                ('add_p', models.TextField(blank=True, null=True)),
                ('match_type', models.TextField(blank=True, null=True)),
                ('geocoder', models.TextField(blank=True, null=True)),
                ('geometry', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'filings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Judgments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('method', models.TextField(blank=True, null=True)),
                ('for_field', models.TextField(blank=True, db_column='for', null=True)),
                ('against', models.TextField(blank=True, null=True)),
                ('docket', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'judgments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plaintiffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('docket', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plaintiffs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpatialRefSys',
            fields=[
                ('srid', models.IntegerField(primary_key=True, serialize=False)),
                ('auth_name', models.CharField(blank=True, max_length=256, null=True)),
                ('auth_srid', models.IntegerField(blank=True, null=True)),
                ('srtext', models.CharField(blank=True, max_length=2048, null=True)),
                ('proj4text', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'db_table': 'spatial_ref_sys',
                'managed': False,
            },
        ),
    ]
