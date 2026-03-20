def urutkan_angka(data, jenis_urutan="ascending"):
    if not isinstance(data, list):
        print("Salah: Input harus berupa list.")
        return None
    if not all(isinstance(x, (int, float)) for x in data):
        print("Salah: List harus berisi angka (integer atau float).")
        return None
    if jenis_urutan not in ["ascending", "descending"]:
        print("Salah: Jenis urutan harus 'ascending' atau 'descending'.")
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

print("=== Program Pengurutan Angka ===\n")

while True:
    try:
        raw = input("Masukkan angka-angka (pisahkan dengan spasi): ")
        angka = [float(x) if '.' in x else int(x) for x in raw.strip().split()]
        if len(angka) == 0:
            print("Salah: masukkan minimal satu angka.\n")
            continue
        break
    except ValueError:
        print("Salah: Pastikan inputannya hanya berisi angka.\n")

while True:
    jenis = input("Pilih jenis urutan (ascending / descending): ").strip().lower()
    if jenis in ["ascending", "descending"]:
        break
    print("Salah: Ketik 'ascending' atau 'descending'.\n")

hasil = urutkan_angka(angka, jenis)
print(f"\nData Awal   : {angka}")
print(f"jenis Urutan nya: {jenis}")
print(f"Hasil Urutan nya: {hasil}")