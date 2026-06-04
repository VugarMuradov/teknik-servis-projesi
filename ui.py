from bl import BusinessLayer

class PresentationLayer:
    def __init__(self):
        # Arayüz katmanı, işleri yürütmek için Business Layer (Aşçı) katmanını çağırır.
        self.bl = BusinessLayer()

    def ana_menu(self):
        while True:
            print("\n" + "="*50)
            print("     TEKNİK SERVİS OTOMASYONU (N-KATMANLI)     ")
            print("="*50)
            print(" [MÜŞTERİ & CİHAZ İŞLEMLERİ]")
            print("  1 - Yeni Müşteri Ekle")
            print("  2 - Müşterileri Listele")
            print("  3 - Müşteriye Yeni Cihaz Ekle")
            print("  4 - Tüm Cihazları Listele")
            print("-" * 50)
            print(" [PERSONEL & ARIZA İŞLEMLERİ]")
            print("  5 - Yeni Personel Ekle")
            print("  6 - Personelleri Listele")
            print("  7 - Yeni Arıza Kaydı Aç (Beklemede)")
            print("  8 - Arıza Kayıtlarını Listele")
            print("-" * 50)
            print(" [TEKNİK SERVİS & STOK İŞLEMLERİ]")
            print("  9 - Yeni Yedek Parça Ekle (Stok)")
            print(" 10 - Yedek Parçaları Listele")
            print(" 11 - Cihaza Servis İşlemi Uygula (Tamir)")
            print(" 12 - Servis İşlemlerini Listele")
            print(" 13 - Tamirde Yedek Parça Kullan (Stoktan Düşer)")
            print("-" * 50)
            print(" [MUHASEBE & ÖDEME]")
            print(" 14 - Ödeme Al / Faturalandır")
            print(" 15 - Tüm Ödemeleri Listele")
            print("="*50)
            print("  0 - Programdan Güvenli Çıkış")
            print("="*50)
            
            secim = input("Lütfen yapmak istediğiniz işlemin numarasını yazın: ")
            
            if secim == "1":
                print("\n--- YENİ MÜŞTERİ EKLEME ---")
                ad = input("Müşteri Adı: ")
                soyad = input("Müşteri Soyadı: ")
                tel = input("Telefon Numarası: ")
                email = input("E-posta Adresi: ")
                adres = input("Açık Adres: ")
                durum, mesaj = self.bl.musteri_ekle(ad, soyad, tel, email, adres)
                print("\n" + mesaj)
                
            elif secim == "2":
                print("\n--- KAYITLI MÜŞTERİLER ---")
                musteriler = self.bl.musteri_listele()
                if musteriler:
                    print("ID | AD SOYAD | TELEFON | E-POSTA | ADRES")
                    print("-" * 60)
                    for m in musteriler:
                        print(f"{m[0]} | {m[1]} {m[2]} | {m[3]} | {m[4]} | {m[5]}")
                else:
                    print("Sistemde kayıtlı müşteri bulunamadı.")
                    
            elif secim == "3":
                print("\n--- YENİ CİHAZ EKLEME ---")
                m_id = input("Cihazın ait olduğu Müşteri ID: ")
                marka = input("Cihaz Markası: ")
                model = input("Cihaz Modeli: ")
                seri = input("Seri Numarası: ")
                tip = input("Cihaz Tipi (Telefon/Bilgisayar vb.): ")
                durum, mesaj = self.bl.cihaz_ekle(m_id, marka, model, seri, tip)
                print("\n" + mesaj)

            elif secim == "4":
                print("\n--- SİSTEMDEKİ CİHAZLAR ---")
                cihazlar = self.bl.cihaz_listele()
                if cihazlar:
                    print("CihazID | MüşteriID | Marka/Model | Seri No | Tip")
                    print("-" * 60)
                    for c in cihazlar:
                        print(f"{c[0]} | {c[1]} | {c[2]} {c[3]} | {c[4]} | {c[5]}")
                else:
                    print("Sistemde kayıtlı cihaz bulunamadı.")

            elif secim == "5":
                print("\n--- YENİ PERSONEL EKLEME ---")
                ad = input("Personel Adı: ")
                soyad = input("Personel Soyadı: ")
                tel = input("Telefon Numarası: ")
                uzmanlik = input("Uzmanlık Alanı (Örn: Apple, Anakart, Yazılım): ")
                durum, mesaj = self.bl.personel_ekle(ad, soyad, tel, uzmanlik)
                print("\n" + mesaj)

            elif secim == "6":
                print("\n--- SİSTEMDEKİ PERSONELLER ---")
                personeller = self.bl.personel_listele()
                if personeller:
                    print("ID | AD SOYAD | TELEFON | UZMANLIK ALANI")
                    print("-" * 60)
                    for p in personeller:
                        print(f"{p[0]} | {p[1]} {p[2]} | {p[3]} | {p[4]}")
                else:
                    print("Sistemde kayıtlı personel bulunamadı.")

            elif secim == "7":
                print("\n--- YENİ ARIZA KAYDI AÇMA ---")
                c_id = input("Arızalı Cihazın ID'si: ")
                p_id = input("Atanacak Personel ID'si: ")
                aciklama = input("Arıza Şikayeti / Açıklama: ")
                durum, mesaj = self.bl.ariza_ekle(c_id, p_id, aciklama)
                print("\n" + mesaj)

            elif secim == "8":
                print("\n--- TÜM ARIZA KAYITLARI ---")
                arizalar = self.bl.ariza_listele()
                if arizalar:
                    print("ArızaID | CihazID | PersonelID | Açıklama | Tarih | Durum")
                    print("-" * 70)
                    for a in arizalar:
                        print(f"{a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]}")
                else:
                    print("Sistemde arıza kaydı bulunamadı.")

            elif secim == "9":
                print("\n--- YENİ YEDEK PARÇA EKLEME ---")
                adi = input("Parça Adı (Örn: iPhone 11 Ekran, 8GB DDR4 RAM): ")
                stok = input("Başlangıç Stok Miktarı: ")
                fiyat = input("Birim Fiyatı (TL): ")
                durum, mesaj = self.bl.parca_ekle(adi, stok, fiyat)
                print("\n" + mesaj)

            elif secim == "10":
                print("\n--- YEDEK PARÇA STOK DURUMU ---")
                parcalar = self.bl.parca_listele()
                if parcalar:
                    print("ParçaID | Parça Adı | Stok Miktarı | Birim Fiyat")
                    print("-" * 60)
                    for p in parcalar:
                        print(f"{p[0]} | {p[1]} | {p[2]} Adet | {p[3]} TL")
                else:
                    print("Stokta yedek parça bulunamadı.")

            elif secim == "11":
                print("\n--- SERVİS İŞLEMİ (TAMİR) KAYDET ---")
                a_id = input("Hangi Arıza ID'sine işlem yapılıyor?: ")
                aciklama = input("Yapılan Teknik Müdahale Açıklaması: ")
                iscilik = input("İşçilik Ücreti (TL): ")
                durum, mesaj = self.bl.servis_islem_ekle(a_id, aciklama, iscilik)
                print("\n" + mesaj)

            elif secim == "12":
                print("\n--- YAPILAN SERVİS İŞLEMLERİ ---")
                islemler = self.bl.servis_islem_listele()
                if islemler:
                    print("ServisID | ArızaID | Yapılan İşlem | Tarih | İşçilik")
                    print("-" * 60)
                    for i in islemler:
                        print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} TL")
                else:
                    print("Henüz yapılmış bir servis işlemi bulunamadı.")

            elif secim == "13":
                print("\n--- TAMİRDE YEDEK PARÇA KULLAN ---")
                s_id = input("Hangi Servis (İşlem) ID'sinde parça kullanıldı?: ")
                p_id = input("Kullanılan Yedek Parça ID'si: ")
                miktar = input("Kaç Adet Kullanıldı?: ")
                durum, mesaj = self.bl.kullanilan_parca_ekle(s_id, p_id, miktar)
                print("\n" + mesaj)

            elif secim == "14":
                print("\n--- ÖDEME ALMA VE FATURALANDIRMA ---")
                s_id = input("Ödemesi alınacak Servis ID: ")
                tutar = input("Toplam Tutar (İşçilik + Parça Maliyeti): ")
                tip = input("Ödeme Tipi (Nakit / Kredi Kartı / Havale): ")
                durum, mesaj = self.bl.odeme_ekle(s_id, tutar, tip)
                print("\n" + mesaj)

            elif secim == "15":
                print("\n--- MUHASEBE / TÜM ÖDEME KAYITLARI ---")
                odemeler = self.bl.odeme_listele()
                if odemeler:
                    print("ÖdemeID | ServisID | Toplam Tutar | Fatura Tarihi | Ödeme Tipi")
                    print("-" * 70)
                    for o in odemeler:
                        print(f"{o[0]} | {o[1]} | {o[2]} TL | {o[3]} | {o[4]}")
                else:
                    print("Sistemde henüz bir ödeme kaydı bulunamadı.")

            elif secim == "0":
                print("\nOtomasyon güvenli bir şekilde kapatılıyor. İyi çalışmalar!")
                break
            else:
                print("\nGeçersiz seçim! Lütfen menüdeki numaralardan birini yazın.")

if __name__ == "__main__":
    app = PresentationLayer()
    app.ana_menu()