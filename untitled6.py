# Fungsi untuk menentukan harga tiket berdasarkan umur
def hitung_harga_tiket(umur):
    # Umur kurang dari atau sama dengan 2 tahun
    if umur <= 2:
        return 0  # Gratis
    # Umur 3 tahun sampai 12 tahun
    elif umur >= 3 and umur <= 12:
        return 14  # $14
    # Umur 65 tahun ke atas
    elif umur >= 65:
        return 18  # $18
    # Kategori Umum (selain kriteria di atas)
    else:
        return 23  # $23

# Program Utama
def main():
    print("Program Tiket Kebun Binatang")
    print("----------------------------")
    
    total_harga = 0.0
    counter = 1
    
    # Loop untuk meminta input umur secara berulang
    while True:
        try:
            # Meminta input umur dari user. Input '0' atau 'selesai' dapat digunakan untuk mengakhiri.
            umur_input = input(f"Masukkan umur {counter} (atau ketik 'done' untuk selesai): ").strip()
            
            if umur_input.lower() == 'done' or not umur_input:
                break # Keluar dari loop jika input 'done' atau kosong
            
            umur = int(umur_input)
            
            # Hitung harga tiket menggunakan fungsi
            harga_tiket = hitung_harga_tiket(umur)
            
            # Tambahkan ke total harga
            total_harga += harga_tiket
            
            # Tampilkan rincian
            print(f"Harga Tiket: ${harga_tiket}.00")
            print(f"Running total: ${total_harga:.2f}")
            
            counter += 1
            
        except ValueError:
            # Keluar dari loop jika input bukan angka
            if umur_input:
                 print("Input tidak valid. Silakan masukkan angka untuk umur.")
            break 
    
    print("\n--- Pembayaran ---")
    print(f"Total biaya keseluruhan: ${total_harga:.2f}")
    
    # Perhitungan kembalian
    if total_harga > 0:
        while True:
            try:
                uang_bayar = float(input("Masukkan jumlah uang: "))
                if uang_bayar < total_harga:
                    print(f"Uang kurang ${total_harga - uang_bayar:.2f}. Mohon tambah pembayaran.")
                    continue
                
                kembalian = uang_bayar - total_harga
                print(f"Running Kembalian: ${kembalian:.2f}")
                break
            except ValueError:
                print("Input uang tidak valid. Masukkan angka.")
    else:
        print("Tidak ada tiket yang dibeli.")

# Menjalankan program utama
if __name__ == "__main__":
    main()

