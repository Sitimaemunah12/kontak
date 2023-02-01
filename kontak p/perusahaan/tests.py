from django.test import TestCase
from .models import Perusahaan
# from django.core.exceptions import ObjectDoesNotExist
class SiswaTestCase(TestCase):
    def setUp(self):
        Perusahaan.objects.create( nama_perusahaan="PT. Sejahtera", email="Sejahtera@gmail.com")
        
    def test_perus_cek_nama(self):
        """cek nama Perusahaan"""
        smkn1= Perusahaan.objects.get(nama_perusahaan="PT. Sejahtera")
        self.assertEqual(smkn1.nama_perusahaan, "PT. Sejahtera")
            
    def test_update(self):
# create
        instance = Perusahaan(nama_perusahaan='PT. Sejahtera', email='Sejahtera@gmail.com')
        instance.save()
# update
        instance.nama_perusahaan = 'PT. Talenta'
        instance.save()
        
        update_instance = Perusahaan.objects.get(id=instance.id)
        self.assertEqual(update_instance.nama_perusahaan, 'PT. Talenta')

    def test_read(self):
        instance = Perusahaan(nama_perusahaan='PT. Sejahtera',)
        instance.save()
        retrieved_instance = Perusahaan.objects.get(id=instance.id)
        self.assertEqual(retrieved_instance.nama_perusahaan, 'PT. Sejahtera')
        
    def test_delete(self):
        instance=Perusahaan.objects.get(id= 1).delete()[0]
        self.assertEqual(instance, 1)
     

# Create your tests here.

