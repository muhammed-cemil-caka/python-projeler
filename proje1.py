import sqlite3

baglanti = sqlite3.connect('adres_defteri.db')
imlec = baglanti.cursor()

imlec.execute('''CREATE TABLE IF NOT EXISTS kisiler (
                    id INTEGER PRIMARY KEY,
                    ad TEXT,
                    soyad TEXT,
                    telefon TEXT,
                    email TEXT
                )''')

def kisi_ekle(ad, soyad, telefon, email):
    imlec.execute('''INSERT INTO kisiler (ad, soyad, telefon, email)
                    VALUES (?, ?, ?, ?)''', (ad, soyad, telefon, email))
    baglanti.commit()
    print("Kişi başarıyla eklendi.")

def kisileri_listele():
    imlec.execute('''SELECT * FROM kisiler''')
    kisiler = imlec.fetchall()
    if kisiler:
        print("Adres Defteri:")
        for kisi in kisiler:
            print(f"ID: {kisi[0]}, Ad: {kisi[1]}, Soyad: {kisi[2]}, Telefon: {kisi[3]}, Email: {kisi[4]}")
    else:
        print("Adres defteriniz şu anda boş.")

def kisi_sil(kisi_id):
    imlec.execute('''DELETE FROM kisiler WHERE id = ?''', (kisi_id,))
    baglanti.commit()
    print("Kişi başarıyla silindi.")

def kisi_guncelle(kisi_id, ad, soyad, telefon, email):
    imlec.execute('''UPDATE kisiler SET ad = ?, soyad = ?, telefon = ?, email = ? WHERE id = ?''',
                    (ad, soyad, telefon, email, kisi_id))
    baglanti.commit()
    print("Kişi bilgileri başarıyla güncellendi.")

def ana_menu_goster():
    print("\nAdres Defteri Uygulaması")
    print("1. Kişi Ekle")
    print("2. Kişileri Listele")
    print("3. Kişi Sil")
    print("4. Kişi Bilgilerini Güncelle")
    print("5. Çıkış")

if __name__ == "__main__":
    while True:
        ana_menu_goster()
        secim = input("Yapmak istediğiniz işlemi seçin: ")

        if secim == '1':
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            telefon = input("Telefon: ")
            email = input("Email: ")
            kisi_ekle(ad, soyad, telefon, email)
        elif secim == '2':
            kisileri_listele()
        elif secim == '3':
            kisi_id = input("Silmek istediğiniz kişinin ID'sini girin: ")
            kisi_sil(kisi_id)
        elif secim == '4':
            kisi_id = input("Güncellemek istediğiniz kişinin ID'sini girin: ")
            ad = input("Yeni ad: ")
            soyad = input("Yeni soyad: ")
            telefon = input("Yeni telefon: ")
            email = input("Yeni email: ")
            kisi_guncelle(kisi_id, ad, soyad, telefon, email)
        elif secim == '5':
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
