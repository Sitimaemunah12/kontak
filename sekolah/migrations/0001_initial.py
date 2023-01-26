# Generated by Django 4.1.5 on 2023-01-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sekolah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npsn', models.CharField(blank=True, max_length=20)),
                ('nama_smk', models.CharField(max_length=50)),
                ('Status', models.CharField(choices=[('Swasta', 'Swasta'), ('Negeri', 'Negeri')], max_length=15)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('provinsi', models.CharField(max_length=50)),
                ('kabupaten_kota', models.CharField(max_length=50)),
                ('kecamatan', models.CharField(max_length=50)),
                ('telp', models.CharField(blank=True, max_length=13, null=True)),
                ('fax', models.CharField(blank=True, max_length=13, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
