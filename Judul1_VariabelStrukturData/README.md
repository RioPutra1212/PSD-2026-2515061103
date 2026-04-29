def menu():
    print("1. Tampilkan address array")
    print("2. Tampilkan address dari semua hari")
    print("3. Masukkan jumlah penjualan selama 7 hari")
    print("4. cek isi penjualan hari tertentu")
    print("5. jumlah keseluruhan penjualan selama 7 hari")
    print("6. jumlah pengeluaran dalam 7 hari")
    print("7. Masukkan jumlah pengeluaran selama 7 hari")
    print("8. Keluar")

Baris ini membuat sebuah fungsi bernama menu(). Fungsi ini digunakan untuk menampilkan daftar pilihan menu pada program
Menampilkan pilihan menu nomor 1 untuk melihat alamat memori dari array penjualan
Menampilkan pilihan menu nomor 2 untuk melihat alamat memori setiap elemen dalam array
Pilihan menu nomor 3 untuk menginput data penjualan selama 7 hari.
Pilihan menu nomor 4 untuk mengecek jumlah penjualan pada hari tertentu.
Pilihan menu nomor 5 untuk menghitung total semua penjualan selama 7 hari.
Pilihan menu nomor 6 untuk menghitung total semua pengeluaran selama 7 hari.
Pilihan menu nomor 7 untuk menginput data pengeluaran selama 7 hari.
Pilihan menu nomor 8 untuk keluar dari program.
    


def main():
    penjualan = [0] * 7   # 7 hari (Senin - Minggu)
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

Membuat fungsi utama bernama main() yang akan menjalankan seluruh program.
Membuat list penjualan yang berisi 7 angka nol. Ini digunakan untuk menyimpan data penjualan dari Senin sampai Minggu.
Membuat list hari yang berisi nama-nama hari dalam seminggu.

    pengeluaran = [0] * 7  # 7 hari (Senin - Minggu)  
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
            
Membuat list pengeluaran yang berisi 7 angka nol untuk menyimpan data pengeluaran selama 7 hari.
Variabel running digunakan untuk mengontrol perulangan program. Jika True, program akan terus berjalan.
Perulangan while akan terus berjalan selama running bernilai True.
Memanggil fungsi menu() agar daftar pilihan ditampilkan.
Digunakan untuk mencoba menjalankan kode yang mungkin menghasilkan error.
User diminta memasukkan pilihan menu. Input diubah menjadi tipe integer.
Jika input bukan angka, maka akan masuk ke bagian ini.
Menampilkan pesan error jika input salah.
Mengulang kembali ke awal while.

        if choice == 1:
            print(f"Address array penjualan: {id(penjualan)}")

Jika user memilih menu 1.
Menampilkan alamat memori dari list penjualan menggunakan fungsi id().

        elif choice == 2:
            for i in range(7):
                print(f"Address penjualan {hari[i]}: {id(penjualan[i])}")

Jika memilih menu 2.
Perulangan dari 0 sampai 6 untuk semua hari.
Menampilkan alamat memori dari setiap isi list penjualan.

        elif choice == 3:
            print("Masukkan jumlah penjualan selama 7 hari:")
            for i in range(7):
                while True:
                    try:
                        penjualan[i] = int(input(f"{hari[i]} = "))
                        break
                    except ValueError:
                        print("Input tidak valid, masukkan angka!")

            print("Data penjualan:")
            for i in range(7):
                print(f"{hari[i]}: {penjualan[i]}")
Jika memilih menu 3.
Menampilkan instruksi input data penjualan.
Loop untuk input 7 hari.
Loop agar input terus diminta sampai benar.
Mencoba menjalankan input angka.
User memasukkan jumlah penjualan sesuai hari, lalu disimpan ke list.
Jika input berhasil, keluar dari loop.
Jika input bukan angka.
Menampilkan pesan error
Menampilkan hasil input.
Loop menampilkan semua data.
Menampilkan penjualan tiap hari.       

        elif choice == 4:
            while True:
                try:
                    hari_ke = int(input("Masukkan nomor hari (1-7): ")) - 1
                    if 0 <= hari_ke < 7:
                        print(f"Jumlah penjualan {hari[hari_ke]}: {penjualan[hari_ke]}")
                        break
                    else:
                        print("Nomor hari tidak valid!")
                except ValueError:
                    print("Input tidak valid, masukkan angka!")
                    

Jika memilih menu 4.
Loop agar input hari valid.
Mencoba input angka.
User memasukkan nomor hari, lalu dikurangi 1 karena index list dimulai dari 0.
Mengecek apakah nomor hari valid.
Menampilkan jumlah penjualan pada hari yang dipilih.
Keluar dari loop.
Jika nomor hari salah.
Pesan error.
Jika input bukan angka.
Pesan error.

        elif choice == 5:
            total_penjualan = sum(penjualan)
            print(f"Jumlah keseluruhan penjualan selama 7 hari: {total_penjualan}")

Jika memilih menu 5.
Menghitung total seluruh penjualan menggunakan fungsi sum().
Menampilkan hasil total penjualan.


        elif choice == 6:
            total_pengeluaran = sum(pengeluaran)
            print(f"Jumlah keseluruhan pengeluaran selama 7 hari: {total_pengeluaran}")

Jika memilih menu 6.
Menghitung total seluruh pengeluaran.
Menampilkan total pengeluaran.


        elif choice == 7:
            print("Masukkan jumlah pengeluaran selama 7 hari:")
            for i in range(7):
                while True:
                    try:
                        pengeluaran[i] = int(input(f"{hari[i]} = "))
                        break
                    except ValueError:
                        print("Input tidak valid, masukkan angka!")

Jika memilih menu 7.

Bagian ini sama seperti input penjualan, tetapi digunakan untuk pengeluaran.                        

            print("Data pengeluaran:")
            for i in range(7):
                print(f"{hari[i]}: {pengeluaran[i]}")

        elif choice == 8:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")
            
Jika memilih menu 8.
Menghentikan perulangan program.
Menampilkan pesan program selesai.
Jika pilihan menu tidak sesuai.
Menampilkan pesan error.

if __name__ == "__main__":
    main()
Mengecek apakah file dijalankan langsung.
Menjalankan fungsi utama main().
