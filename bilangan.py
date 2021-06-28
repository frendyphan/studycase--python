from operator import truediv
import statistics
from numpy.core.defchararray import array, index
from numpy.lib.function_base import median



jumlsh = 1
data_angka = []
kali = 1

banyak = int(input("berapa banyak angka yang akan dimasukan? "))
for i in range(banyak):
    data_angka.append(int(input("masukan angka: ")))

    kali *= data_angka[i]
    median =statistics.median(data_angka)
    rerata = statistics.mean(data_angka)
    data_angka.sort()
    print(data_angka)
    
    print ('kali = {} '.format(kali))
    print(f'rata-rata -> {rerata}')
    print(f'NilaiTengah -> {median}')
    



