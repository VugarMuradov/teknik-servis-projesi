from dal import DataAccessLayer

class BusinessLayer:
    def __init__(self):
        # İş yapabilmek için arka planda DAL (Depocu) katmanını ayağa kaldırıyoruz.
        self.dal = DataAccessLayer()

    # ==========================================
    # 1. MÜŞTERİ İŞ MANTIĞI
    # ==========================================
    def musteri_ekle(self, ad, soyad, telefon, email, adres):
        if not ad.strip() or not soyad.strip():
            return False, "Hata: Müşteri adı ve soyadı boş bırakılamaz!"
        self.dal.musteri_ekle(ad, soyad, telefon, email, adres)
        return True, "Müşteri başarıyla eklendi! (Arka planda TRIGGER çalıştı ve harfler büyütüldü)."

    def musteri_listele(self):
        return self.dal.musteri_listele()

    def musteri_guncelle(self, m_id, ad, soyad, telefon, email, adres):
        if not m_id.strip():
            return False, "Hata: Güncellenecek müşterinin ID bilgisini girmelisiniz!"
        self.dal.musteri_guncelle(int(m_id), ad, soyad, telefon, email, adres)
        return True, f"ID'si {m_id} olan müşterinin bilgileri başarıyla güncellendi."

    def musteri_sil(self, m_id):
        if not m_id.strip():
            return False, "Hata: Silinecek müşterinin ID bilgisini girmelisiniz!"
        self.dal.musteri_sil(int(m_id))
        return True, f"ID'si {m_id} olan müşteri sistemden silindi."

    # ==========================================
    # 2. CİHAZ İŞ MANTIĞI
    # ==========================================
    def cihaz_ekle(self, m_id, marka, model, seri_no, cihaz_tipi):
        if not m_id.strip() or not marka.strip() or not model.strip():
            return False, "Hata: Müşteri ID, Marka ve Model alanları boş bırakılamaz!"
        self.dal.cihaz_ekle(int(m_id), marka, model, seri_no, cihaz_tipi)
        return True, "Cihaz kaydı başarıyla yapıldı."

    def cihaz_listele(self):
        return self.dal.cihaz_listele()

    # ==========================================
    # 3. PERSONEL İŞ MANTIĞI
    # ==========================================
    def personel_ekle(self, ad, soyad, telefon, uzmanlik):
        if not ad.strip() or not soyad.strip() or not uzmanlik.strip():
            return False, "Hata: Personel adı, soyadı ve uzmanlık alanı boş bırakılamaz!"
        self.dal.personel_ekle(ad, soyad, telefon, uzmanlik)
        return True, "Yeni personel sisteme başarıyla kaydedildi."

    def personel_listele(self):
        return self.dal.personel_listele()

    # ==========================================
    # 4. ARIZA KAYITLARI İŞ MANTIĞI
    # ==========================================
    def ariza_ekle(self, cihaz_id, personel_id, aciklama):
        if not cihaz_id.strip() or not personel_id.strip() or not aciklama.strip():
            return False, "Hata: Cihaz ID, Personel ID ve Arıza Açıklaması zorunludur!"
        self.dal.ariza_ekle(int(cihaz_id), int(personel_id), aciklama)
        return True, "Arıza kaydı başarıyla açıldı (Durum: Beklemede)."

    def ariza_listele(self):
        return self.dal.ariza_listele()

    def ariza_guncelle(self, ariza_id, cihaz_id, personel_id, aciklama, durum):
        if not ariza_id.strip():
            return False, "Hata: Güncellenecek Arıza ID belirtilmelidir!"
        self.dal.ariza_guncelle(int(ariza_id), int(cihaz_id), int(personel_id), aciklama, durum)
        return True, f"ID'si {ariza_id} olan arıza kaydı başarıyla güncellendi."

    # ==========================================
    # 5. YEDEK PARÇA İŞ MANTIĞI
    # ==========================================
    def parca_ekle(self, adi, stok, fiyat):
        if not adi.strip():
            return False, "Hata: Parça adı boş bırakılamaz!"
        # İŞ KURALI (CHECK kısıtlaması simülasyonu): Stok ve fiyat negatif olamaz
        if int(stok) < 0 or float(fiyat) <= 0:
            return False, "Hata: Stok miktarı 0'dan küçük, birim fiyat 0 veya daha az olamaz!"
        
        self.dal.parca_ekle(adi, int(stok), float(fiyat))
        return True, "Yedek parça stoğu başarıyla eklendi."

    def parca_listele(self):
        return self.dal.parca_listele()

    # ==========================================
    # 6. SERVİS İŞLEMLERİ İŞ MANTIĞI
    # ==========================================
    def servis_islem_ekle(self, ariza_id, aciklama, iscilik):
        if not ariza_id.strip() or not aciklama.strip():
            return False, "Hata: Arıza ID ve yapılan işlem açıklaması zorunludur!"
        if float(iscilik) < 0:
            return False, "Hata: İşçilik ücreti negatif olamaz!"
        
        self.dal.servis_islem_ekle(int(ariza_id), aciklama, float(iscilik))
        return True, "Servis işlemi (tamir aşaması) başarıyla kaydedildi."

    def servis_islem_listele(self):
        return self.dal.servis_islem_listele()

    # ==========================================
    # 7. KULLANILAN PARÇALAR İŞ MANTIĞI
    # ==========================================
    def kullanilan_parca_ekle(self, servis_id, parca_id, miktar):
        if not servis_id.strip() or not parca_id.strip() or not miktar.strip():
            return False, "Hata: Tüm alanların doldurulması zorunludur!"
        if int(miktar) <= 0:
            return False, "Hata: Kullanılan parça miktarı en az 1 olmalıdır!"
        
        self.dal.kullanılan_parca_ekle(int(servis_id), int(parca_id), int(miktar))
        return True, "Parça servis işlemine başarıyla eklendi! (Arka planda TRIGGER çalıştı ve stok düştü)."

    # ==========================================
    # 8. ÖDEMELER İŞ MANTIĞI
    # ==========================================
    def odeme_ekle(self, servis_id, tutar, tip):
        if not servis_id.strip() or not tutar.strip() or not tip.strip():
            return False, "Hata: Servis ID, Tutar ve Ödeme Tipi boş bırakılamaz!"
        if float(tutar) < 0:
            return False, "Hata: Ödeme tutarı negatif olamaz!"
            
        self.dal.odeme_ekle(int(servis_id), float(tutar), tip)
        return True, "Ödeme kaydı başarıyla alındı ve faturalandırıldı."

    def odeme_listele(self):
        return self.dal.odeme_listele()