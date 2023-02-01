from django.test import TestCase
from .models import siswa
# from django.core.exceptions import ObjectDoesNotExist
class SiswaTestCase(TestCase):
    def setUp(self):
        siswa.objects.create( NAMA="Siti maemunah", tanggal_lahir="2023-01-30")
        
    def test_siswa_cek_nama(self):
        """cek nama siswa"""
        smkn1= siswa.objects.get(NAMA="Siti maemunah")
        self.assertEqual(smkn1.NAMA, "Siti maemunah")
            
    def test_update(self):
# create
        instance = siswa(NAMA='Siti maemunah', tanggal_lahir='2023-01-30')
        instance.save()
# update
        instance.NAMA = 'Siti Zira'
        instance.save()
        
        update_instance = siswa.objects.get(id=instance.id)
        self.assertEqual(update_instance.NAMA, 'Siti Zira')

    def test_read(self):
        instance = siswa(NAMA='Siti maemunah',)
        instance.save()
        retrieved_instance = siswa.objects.get(id=instance.id)
        self.assertEqual(retrieved_instance.NAMA, 'Siti maemunah')
        
    def test_delete(self):
        instance=siswa.objects.get(id= 1).delete()[0]
        self.assertEqual(instance, 1)
# create your tests here       

