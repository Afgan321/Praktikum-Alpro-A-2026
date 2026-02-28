angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

"""
kode program tersebut meminta 1 masukan

ketika diinput angka nol maka terjadinya
Masukkan index (0-2): 0
Nilai: 10
Selesai.

ketika diinput huruf maka yang terjadi
Masukkan index (0-2): f
Harus berupa angka bulat!
Selesai

ketika diinput huruf maka yang terjadi
Masukkan index (0-2): -2
Nilai: 20
Selesai. 
"""

