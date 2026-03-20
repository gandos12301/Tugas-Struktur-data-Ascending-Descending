def urutkan_angka(data, jenis_urutan="ascending"):
    if not isinstance(data, list):
        print("salah: Input harus berupa list.")
        return None

    if not all(isinstance(x, (int, float)) for x in data):
        print("salah: List harus berisi angka (integer atau float).")
        return None

    if jenis_urutan not in ["ascending", "descending"]:
        print("salah : Jenis urutan harus 'ascending' atau 'descending'.")
        return None

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

angka = [90, 50, 33, 67, 90, 12, 45]

angka_urut_naik = urutkan_angka(angka)
print(f"Urutan Menaik: {angka_urut_naik}")

angka_urut_turun = urutkan_angka(angka, "descending")
print(f"Urutan Menurun: {angka_urut_turun}")

hasil = urutkan_angka("bukan list", "ascending")
print(hasil)