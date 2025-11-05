#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 14:19:36 2025

@author: ebenpolii
"""

# Fungsi untuk mengkonversi nilai huruf ke nilai angka
def hitung_nilai_huruf(nilai_kategori):
    # Menggunakan kamus (dictionary) untuk pemetaan nilai
    skala_nilai = {
        "A": 4.00,
        "A-": 3.75,
        "B+": 3.50,
        "B": 3.00,
        "B-": 2.75,
        "C+": 2.50,
        "C": 2.00,
        "C-": 1.75,
        "D": 1.50,
        "E": 1.25
    }
    
    # Menggunakan struktur percabangan untuk mendapatkan nilai angka
    # Mengabaikan huruf besar/kecil (case-insensitive)
    nilai_kategori_upper = nilai_kategori.upper()
    
    if nilai_kategori_upper in skala_nilai:
        return skala_nilai[nilai_kategori_upper]
    else:
        # Mengembalikan 0 atau nilai default jika input tidak valid
        return 0.00 

# Program Utama
def main():
    print("Program Penilaian Nilai Kategori")
    print("--------------------------------")
    
    # List untuk menyimpan nilai angka (poin)
    daftar_nilai_angka = []
    
    # Loop untuk meminta input 5 nilai
    for i in range(1, 6):
        while True:
            # Meminta input nilai kategori dari user
            nilai_input = input(f"Masukkan nilai {i}: ").strip()
            
            # Mendapatkan nilai angka (poin) dari fungsi
            nilai_poin = hitung_nilai_huruf(nilai_input)
            
            if nilai_poin > 0:
                print(f"Nilai {nilai_input.upper()} = {nilai_poin}")
                daftar_nilai_angka.append(nilai_poin)
                break  # Keluar dari loop input jika nilai valid
            else:
                print("Nilai tidak valid. Masukkan nilai yang sesuai (A, A-, B+, dst.).")

    print("--------------------------------")
    
    # Menghitung rata-rata nilai
    if daftar_nilai_angka:
        total_nilai = sum(daftar_nilai_angka)
        jumlah_nilai = len(daftar_nilai_angka)
        rata_rata = total_nilai / jumlah_nilai
        print(f"Rata-rata IPZ adalah: {rata_rata:.16f}") # Output sesuai contoh di gambar
    else:
        print("Tidak ada nilai valid yang dimasukkan.")

# Menjalankan program utama
if __name__ == "__main__":
    main()