# Generated by Django 2.1.4 on 2018-12-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('artist_first_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
                'db_table': 'artist',
                'ordering': ['artist_last_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('artwork_id', models.AutoField(primary_key=True, serialize=False)),
                ('accession_number', models.CharField(blank=True, max_length=250, null=True)),
                ('artwork_title', models.CharField(blank=True, max_length=500, null=True)),
                ('artwork_date', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Artwork',
                'verbose_name_plural': 'Artworks',
                'db_table': 'artwork',
                'ordering': ['artwork_title'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArtworkSubject',
            fields=[
                ('artwork_subject_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Arwork Subject',
                'verbose_name_plural': 'Artwork Subjects',
                'db_table': 'artwork_subject',
                'ordering': ['artwork', 'subject'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Era',
            fields=[
                ('era_id', models.AutoField(primary_key=True, serialize=False)),
                ('era_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Era',
                'verbose_name_plural': 'Eras',
                'db_table': 'era',
                'ordering': ['era_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('medium_id', models.AutoField(primary_key=True, serialize=False)),
                ('medium_name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Medium',
                'verbose_name_plural': 'Mediums',
                'db_table': 'medium',
                'ordering': ['medium_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('movement_id', models.AutoField(primary_key=True, serialize=False)),
                ('movement_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Movement',
                'verbose_name_plural': 'Movements',
                'db_table': 'movement',
                'ordering': ['movement_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
                'db_table': 'subject',
                'ordering': ['subject_name'],
                'managed': False,
            },
        ),
    ]
