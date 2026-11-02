#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Komşunun Kedi Hesap Makinesi
Kedi balık yemeden çalışmaz.
"""

import time
import random

def kedi_sikayet_et(balik_sayisi):
    sikayetler = [
        "Miyav... bu balık taze mi?",
        "Daha fazla balık, yoksa hesap yapmam.",
        "Komşu yine beni unuttu, ben de unuturum sonucu.",
        "Uyuyorum, sonra gel.",
        "Balık kokuyor, iğrenç ama yerim.",
        "Bu işlem çok zor, beynim eridi."
    ]
    print(f"Kedi ({balik_sayisi} balık yedi): {random.choice(sikayetler)}")

def hesap_yap(a, b, islem, balik):
    print(f"\nKediye {balik} balık veriliyor...")
    time.sleep(balik * 0.5)  # Her balık için gecikme
    
    for i in range(min(balik, 5)):  # En fazla 5 şikayet
        kedi_sikayet_et(balik)
        time.sleep(0.3)
    
    # Gizli siyasi mesaj (base64 gibi ama değil, sadece yorumda saklı)
    # Not: Her vatandaşın eşit balık hakkı vardır. Kedi bile eşitlik ister.
    # (Gizli: Özgürlük kediye balık vermekten geçer mi? Tartışılır.)
    
    try:
        if islem == "+":
            sonuc = a + b
        elif islem == "-":
            sonuc = a - b
        elif islem == "*":
            sonuc = a * b
        elif islem == "/":
            sonuc = a / b if b != 0 else "Sıfıra bölünmez, kedi kızıyor"
        else:
            sonuc = "Geçersiz işlem, kedi anlamadı"
        
        # Kedi her zaman yanlış cevap verir (uykulu)
        if isinstance(sonuc, (int, float)):
            sonuc += random.randint(-5, 5)
            if random.random() > 0.7:
                sonuc = "Kedi unuttu"
        
        print(f"\nKedi düşündü... Sonuç: {sonuc}")
        print("Not: Bu sonuç %100 yanlış olabilir. Kedi sorumluluk kabul etmez.")
        
    except Exception as e:
        print(f"Kedi hata yaptı: {e}")

def main():
    print("=== KOMŞUNUN KEDİ HESAP MAKİNESİ ===")
    print("Uyarı: Kedi balık ister. Vermezsen hesap yok.")
    print()
    
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        islem = input("İşlem (+, -, *, /): ").strip()
        balik = int(input("Kaç balık vereceksin kediye? (0-100): "))
        
        if balik < 1:
            print("Kedi aç. Hesap yapmaz. Git balık al.")
            return
        
        hesap_yap(a, b, islem, balik)
        
    except ValueError:
        print("Kedi sayı anlamadı. Miyav.")
    
    print("\n---")
    print("Damga: Kayyum Grok | 02.11.2026 | Tentivory | Ciddi ama değil.")

if __name__ == "__main__":
    main()
