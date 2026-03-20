def shorting_angka(data, urutan='ascending'):
    
    if urutan.lower() == 'descending':
        return sorted(data, reverse=True)
    else:
        return sorted(data)


nilai = [90, 50, 33, 67, 90, 12, 85, 45, 99, 78]

print(shorting_angka(nilai))                  
print(shorting_angka(nilai, 'ascending'))
print(shorting_angka(nilai, 'DESCENDING'))   