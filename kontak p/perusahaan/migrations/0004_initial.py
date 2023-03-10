# Generated by Django 4.1.5 on 2023-01-24 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perusahaan', '0003_delete_perusahaan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perusahaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perusahaan', models.CharField(max_length=50)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kategori', models.CharField(choices=[('PT', 'PT'), ('CV', 'CV'), ('Firma', 'Firma'), ('Persero', 'Persero'), ('Pemerintah', 'Pemerintah'), ('Koperasi', 'Koperasi'), ('Perseorangan', 'Perseorangan')], max_length=50)),
                ('bidang', models.CharField(max_length=50)),
                ('daerah', models.TextField(blank=True, null=True)),
                ('nama_pic', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=50)),
                ('hp', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='perusahaan_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
