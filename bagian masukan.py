#Bagian program untuk input Kendaraan
import time
import random

def masukan():
#Tombol kendaraan, dipilih oleh pengguna
    print('Silahkan pilih kendaraan')
    print('1. Kendaraan roda 2              2. Kendaraan roda 4')
    print('3. Kendaraan roda lebih dari 4')
    print('')
    pil = int(input())
#Selesai bagian pengguna

#Bagian petugas
    plat = input('Silahkan masukkan pelat kendaraan :')
    kendaraan = [] #array untuk kendaraan yang masuk
    # Mulai Generate kode untuk pengguna
    #Plat nomor pengguna di acak sehingga walaupun ada yang menemukan tiket
    #dan mencoba membaca QR kodenya, plat nomor pengguna masih aman
    char_list  = list(plat)
    random.shuffle(char_list)
    if(pil == 1): plat = 'M' + ''.join(plat) #M untuk Motor
    if(pil == 2): plat = 'C' + ''.join(plat) #C untuk Mobil
    if(pil == 3): plat = 'B' + ''.join(plat)
    waktu = time.localtime()      #Waktu komputer lokal
    
    kode = plat + str(waktu.tm_mday) + str(waktu.tm_hour) + str(waktu.tm_min) + str(waktu.tm_sec)
    
    #Selesai Generate
    print('Tiket parkir anda: ')
    print(kode)
    #Nanti kodenya  dienkripsi dalam QR code, asumsikan ada program yang mengubah string
    #tersebut menjadi QR code
    kendaraan.append(kode)
#Selesai Bagain Petugas
    print('Silahkan Masuk!')
masukan()
