def menu():
    print("1. Tampilkan address array")
    print("2. Tampilkan address dari semua hari")
    print("3. Masukkan jumlah penjualan selama 7 hari")
    print("4. cek isi penjualan hari tertentu")
    print("5. jumlah keseluruhan penjualan selama 7 hari")
    print("6. jumlah pengeluaran dalam 7 hari")
    print("7. Masukkan jumlah pengeluaran selama 7 hari")
    print("8. Keluar")


def main():
    penjualan = [0] * 7   # 7 hari (Senin - Minggu)
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

    pengeluaran = [0] * 7  # 7 hari (Senin - Minggu)  
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print(f"Address array penjualan: {id(penjualan)}")

        elif choice == 2:
            for i in range(7):
                print(f"Address penjualan {hari[i]}: {id(penjualan[i])}")

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

        elif choice == 5:
            total_penjualan = sum(penjualan)
            print(f"Jumlah keseluruhan penjualan selama 7 hari: {total_penjualan}")

        elif choice == 6:
            total_pengeluaran = sum(pengeluaran)
            print(f"Jumlah keseluruhan pengeluaran selama 7 hari: {total_pengeluaran}")

        elif choice == 7:
            print("Masukkan jumlah pengeluaran selama 7 hari:")
            for i in range(7):
                while True:
                    try:
                        pengeluaran[i] = int(input(f"{hari[i]} = "))
                        break
                    except ValueError:
                        print("Input tidak valid, masukkan angka!")

            print("Data pengeluaran:")
            for i in range(7):
                print(f"{hari[i]}: {pengeluaran[i]}")

        elif choice == 8:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()