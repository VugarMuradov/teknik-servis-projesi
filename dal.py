import mysql.connector

class DataAccessLayer:
    def __init__(self):
        # MySQL Veritabanı Bağlantı Ayarları
        self.config = {
            'user': 'root',
            'password': '20050503vm',  # <--- Buraya MySQL Workbench şifreni yaz!
            'host': 'localhost',
            'database': 'teknikservisdb'
        }

    def _execute_procedure(self, proc_name, args=()):
        """Veritabanında güvenli şekilde Procedure çalıştıran ortak fonksiyon"""
        conn = None
        cursor = None
        result = None
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            
            # Procedure çağrılıyor (.callproc yöntemi)
            cursor.callproc(proc_name, args)
            
            # Eğer listeleme veya fonksiyon sonucu varsa verileri alıyoruz
            for result_set in cursor.stored_results():
                result = result_set.fetchall()
            
            conn.commit()
            return result
        except mysql.connector.Error as err:
            print(f"\n[Veritabanı Hatası]: {err}")
            return None
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ==========================================
    # 1. MÜŞTERİLER TABLOSU METOTLARI
    # ==========================================
    def musteri_ekle(self, ad, soyad, telefon, email, adres):
        return self._execute_procedure('sp_MusteriEkle', (ad, soyad, telefon, email, adres))

    def musteri_listele(self):
        return self._execute_procedure('sp_MusteriListele')

    def musteri_guncelle(self, musteri_id, ad, soyad, telefon, email, adres):
        return self._execute_procedure('sp_MusteriGuncelle', (musteri_id, ad, soyad, telefon, email, adres))

    def musteri_sil(self, musteri_id):
        return self._execute_procedure('sp_MusteriSil', (musteri_id,))

    # ==========================================
    # 2. CİHAZLAR TABLOSU METOTLARI
    # ==========================================
    def cihaz_ekle(self, musteri_id, marka, model, seri_no, cihaz_tipi):
        return self._execute_procedure('sp_CihazEkle', (musteri_id, marka, model, seri_no, cihaz_tipi))

    def cihaz_listele(self):
        return self._execute_procedure('sp_CihazListele')

    def cihaz_guncelle(self, cihaz_id, musteri_id, marka, model, seri_no, cihaz_tipi):
        return self._execute_procedure('sp_CihazGuncelle', (cihaz_id, musteri_id, marka, model, seri_no, cihaz_tipi))

    def cihaz_sil(self, cihaz_id):
        return self._execute_procedure('sp_CihazSil', (cihaz_id,))

    # ==========================================
    # 3. PERSONELLER TABLOSU METOTLARI
    # ==========================================
    def personel_ekle(self, ad, soyad, telefon, uzmanlik):
        return self._execute_procedure('sp_PersonelEkle', (ad, soyad, telefon, uzmanlik))

    def personel_listele(self):
        return self._execute_procedure('sp_PersonelListele')

    def personel_guncelle(self, personel_id, ad, soyad, telefon, uzmanlik):
        return self._execute_procedure('sp_PersonelGuncelle', (personel_id, ad, soyad, telefon, uzmanlik))

    def personel_sil(self, personel_id):
        return self._execute_procedure('sp_PersonelSil', (personel_id,))

    # ==========================================
    # 4. ARIZA KAYITLARI TABLOSU METOTLARI
    # ==========================================
    def ariza_ekle(self, cihaz_id, personel_id, aciklama):
        return self._execute_procedure('sp_ArizaEkle', (cihaz_id, personel_id, aciklama))

    def ariza_listele(self):
        return self._execute_procedure('sp_ArizaListele')

    def ariza_guncelle(self, ariza_id, cihaz_id, personel_id, aciklama, durum):
        return self._execute_procedure('sp_ArizaGuncelle', (ariza_id, cihaz_id, personel_id, aciklama, durum))

    def ariza_sil(self, ariza_id):
        return self._execute_procedure('sp_ArizaSil', (ariza_id,))

    # ==========================================
    # 5. YEDEK PARÇALAR TABLOSU METOTLARI
    # ==========================================
    def parca_ekle(self, adi, stok, fiyat):
        return self._execute_procedure('sp_ParcaEkle', (adi, stok, fiyat))

    def parca_listele(self):
        return self._execute_procedure('sp_ParcaListele')

    def parca_guncelle(self, parca_id, adi, stok, fiyat):
        return self._execute_procedure('sp_ParcaGuncelle', (parca_id, adi, stok, fiyat))

    def parca_sil(self, parca_id):
        return self._execute_procedure('sp_ParcaSil', (parca_id,))

    # ==========================================
    # 6. SERVİS İŞLEMLERİ TABLOSU METOTLARI
    # ==========================================
    def servis_islem_ekle(self, ariza_id, aciklama, iscilik):
        return self._execute_procedure('sp_ServisIslemEkle', (ariza_id, aciklama, iscilik))

    def servis_islem_listele(self):
        return self._execute_procedure('sp_ServisIslemListele')

    def servis_islem_guncelle(self, servis_id, ariza_id, aciklama, iscilik):
        return self._execute_procedure('sp_ServisIslemGuncelle', (servis_id, ariza_id, aciklama, iscilik))

    def servis_islem_sil(self, servis_id):
        return self._execute_procedure('sp_ServisIslemSil', (servis_id,))

    # ==========================================
    # 7. KULLANILAN PARÇALAR TABLOSU METOTLARI
    # ==========================================
    def kullanılan_parca_ekle(self, servis_id, parca_id, miktar):
        return self._execute_procedure('sp_KullanilanParcaEkle', (servis_id, parca_id, miktar))

    def kullanılan_parca_listele(self):
        return self._execute_procedure('sp_KullanilanParcaListele')

    # ==========================================
    # 8. ÖDEMELER TABLOSU METOTLARI
    # ==========================================
    def odeme_ekle(self, servis_id, tutar, tip):
        return self._execute_procedure('sp_OdemeEkle', (servis_id, tutar, tip))

    def odeme_listele(self):
        return self._execute_procedure('sp_OdemeListele')