try :
 angka1 = float(input('Masukkan angka: '))
 angka2 = float(input('Masukkan angka selanjutnya :'))

 print( 'hasil pembagian: ', angka1 / angka2)

except ValueError :
    print('Input harus berupa Angka')

except TypeError : 
    print('operasi salah')

except ZeroDivisionError :
    print('Angka tidak bisa dibagi 0')

finally :
    print('Program selesai')
