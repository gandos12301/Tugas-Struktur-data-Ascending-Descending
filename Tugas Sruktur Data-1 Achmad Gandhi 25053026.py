def urutkan_angka(data, jenis_urutan):
    
    data_urut = data[:]
    n = len(data_urut)

    for i in range(n):
        for j in range(0, n - i - 1):
            if jenis_urutan == "ascending":
                if data_urut[j] > data_urut[j + 1]:
                    data_urut[j], data_urut[j + 1] = data_urut[j + 1], data_urut[j]
            else:
                if data_urut[j] < data_urut[j + 1]:
                    data_urut[j], data_urut[j + 1] = data_urut[j + 1], data_urut[j]

    return data_urut


print("=== Program Pengurutan Angka ===\n")

while True:
    try:
        raw = input("Masukkan angka (pisahkan dengan spasi): ")
        angka = [int(x) for x in raw.split()]

        if len(angka) == 0:
            print("Minimal masukkan satu angka!\n")
        else:
            break
    except ValueError:
        print("Input gak valid! Hanya boleh angka.\n")


while True:
    print("\nPilih jenis urutan:")
    print("1. Ascending  (kecil ke besar)")
    print("2. Descending (besar ke kecil)")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    if pilihan == "1":
        jenis = "ascending"
        break
    elif pilihan == "2":
        jenis = "descending"
        break
    else:
        print("Pilihan gak valid! Masukkan 1 atau 2.")


hasil = urutkan_angka(angka, jenis)

print("\n=== Hasil ===")
print(f"Data Awalnya   : {angka}")
print(f"Jenis Urutannya: {jenis}")
print(f"Hasil Urutannya: {hasil}")