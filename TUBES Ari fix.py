import datetime
import os

data_kartu_nama=[]
data_kartu_nohp=[]
data_kartu_saldo=[]

def registrasi_kartu():
    #Bagian Registrasi Kartu
    print("----------------------------------------------")    
    print("Selamat datang di Ganesha Parking.")
    print("Disini anda dapat membuat kartu membership, sebagai cara untuk membayar secara non-tunai.")

    #Data Kartu disimpan dalam Array
    #No Kartu adalah No Handphone
    
    global data_kartu_nama
    global data_kartu_nohp
    global data_kartu_saldo
    
    #Masukkan Nama
    print("Silahkan masukkan nama anda.")
    x=input()
    data_kartu_nama.append(x)
    #Masukkan No HP
    print("Silahkan masukkan no handphone anda.")
    y=input()
    data_kartu_nohp.append(y)
    acuan = y
    #Masukkan Saldo Awal
    print("Silahkan masukkan saldo awal anda.")
    z=input()
    data_kartu_saldo.append(z)
    os.system('cls')
    #Output No Kartu serta Info lainnya
    print("Berikut adalah informasi dari data yang telah anda masukkan:")
    x = len(data_kartu_nohp)-1
    print("Data Kartu ke ",(x+1))
    print("Nama :", data_kartu_nama[x])
    print("No HP :", data_kartu_nohp[x])
    print("Saldo :", data_kartu_saldo[x])
    print("No Kartu anda adalah",data_kartu_nohp[x])       
    print("")
    input()
    return data_kartu_nohp[x]

def isiulang_kartu():

    global data_kartu_nama
    global data_kartu_nohp
    global data_kartu_saldo

#Bagian Isi Saldo
    print("Selamat datang di Ganesha Parking.")
    print("Disini anda dapat mengisi ulang saldo dari kartu anda.")

    #Input No Kartu
    print("Silahkan masukkan no kartu anda.")
    nokartu_saldo=input()
    #Jika nokartu_saldo ditemukan:
    found = False
    for i in range(len(data_kartu_nohp)):
        if (nokartu_saldo==data_kartu_nohp[i]):
            #Tampilkan Saldo
            print("Saldo anda adalah sebesar",data_kartu_saldo[i])
            #Isi Ulang
            print("Silahkan masukkan jumlah saldo yang ingin anda tambahkan.")
            saldo_tambahan=input()
            data_kartu_saldo[i]=int(data_kartu_saldo[i])+int(saldo_tambahan)
            #Output hasil Saldo Akhir
            print("Saldo total anda sekarang adalah", data_kartu_saldo[i])
            print("Terima kasih.")
            found = True
            input()

    if(found == False): #Jika tidak ditemukan:
        print("Mohon maaf, nomor kartu anda tidak dapat ditemukan.")
        print("Dimohon untuk melakukan registrasi terlebih dahulu.")
        print("Terima kasih.")
        print("")
        input()
        print("Apakah anda ingin melakukan registrasi kartu?")
        print("1. Iya        2. Tidak")
        regis=(input())
        if(regis=='1'):
            registrasi_kartu()
        else:
            print('Terimakasih')
            os.system('cls')
            return False
    return True
def bayar(X):
   
    global data_kartu_nama
    global data_kartu_nohp
    global data_kartu_saldo
    #Bagian Metode Pembayaran
    os.system('cls')
    print("Silakan pilih metode bayar")
    print("1. Tunai")
    print("2. Non-Tunai")
    pil=(input())
    os.system('cls')
    if X[0] == 'M':
        tmp_now = datetime.datetime.now()
        tmp_time = tmp_now.strftime('%H')
        durasi = int(tmp_time)-int(X[-6:-4])
        if(str(tmp_now.strftime('%d')) != str(X[-8:-6])): durasi = 24   #Kasus Ketika kendaraan parkir lebih dari sehari   
        biaya = min(10000, 2000 + (durasi)*500)
        
    elif X[0] == 'C':
        tmp_now = datetime.datetime.now()
        tmp_time = tmp_now.strftime('%H')
        durasi = int(tmp_time)-int(X[-6:-4]) 
        if(tmp_now.strftime('%d') != X[-8:-6]): durasi = 24   #Kasus Ketika kendaraan parkir lebih dari sehari   
        biaya = min(15000, 5000 + (durasi)*500)
    else:
        tmp_now = datetime.datetime.now()
        tmp_time = tmp_now.strftime('%H')
        durasi = int(tmp_time)-int(X[-6:-4]) 
        if(tmp_now.strftime('%d') != X[-8:-6]): durasi = 24  #Kasus Ketika kendaraan parkir lebih dari sehari   
        biaya = min(20000, 10000 + (durasi)*500)
        
    ###Tunai
    #Langsung bayar
    if(pil=='1'):
        print("Silakan masukkan uang anda: ")
        uang_tunai=int(input())
        if (uang_tunai>int(biaya)):
            print("Kembaliannya adalah", (uang_tunai-int(biaya)))
            print("")
        elif(uang_tunai < int(biaya)):
            print("Mohon maaf, Saldo anda tidak mencukupi.")
            print("Silahkan bayar dengan uang yang cukup atau pilih metode pembayaran yang lain")
            input()
            bayar(X)
    ###Non Tunai
    elif(pil=='2'):
        print("Apakah anda ingin melakukan registrasi kartu?")
        print("1. Iya        2. Tidak")
        regis=(input())
        kode_kartu = ''
        if(regis=='1'):
            os.system('cls')
            kode_kartu = registrasi_kartu()
        elif(regis == '2'):
            #Input Kode Kartu (tap)
            os.system('cls')
            print("Silahkan Masukkan Kode Kartu Anda")
            kode_kartu=input()
            os.system('cls')
        else:
            os.system('cls')
            return bayar(X)
        #Ngecek kode_kartu dengan database
        ketemu = False
        for i in range(len(data_kartu_nohp)):
            if (kode_kartu==data_kartu_nohp[i]): 
            #Jika ketemu:
                ketemu = True
                #Keluar Informasi berupa Saldo 
                if(int(data_kartu_saldo[i])<int(biaya)):
                    print("Mohon maaf, Saldo anda tidak mencukupi.")
                    print("Mohon lakukan pengisian ulang saldo.")
                    print("Apakah anda ingin melakukan pengisian ulang saldo anda?")
                    print("1. Iya          2. Tidak")
                    isiulang=(input())
                    os.system('cls')
                    if (isiulang=='1'):
                        isiulang_kartu()
                    else:
                        print("Baik, terima kasih. Mohon melakukan pembayaran dengan metode lainnya.")
                        bayar(X)
                    #Pembayaran Gagal

                else:
                    data_kartu_saldo[i]=int(data_kartu_saldo[i])-int(biaya)
                    print("Transaksi berhasil, sisa saldo:", str(data_kartu_saldo[i]))
                    print("Apakah anda ingin melakukan pengisian ulang saldo anda?")
                    print("1. Iya          2. Tidak")
                    isiulang=(input())
                    os.system('cls')
                    if(isiulang=='1'):
                        isiulang2 = '1'
                        if(isiulang_kartu() == False):
                            while((isiulang2 == '1')):
                                print("Apakah anda ingin melakukan pengisian ulang saldo anda?")
                                print("1. Iya          2. Tidak")
                                isiulang2=(input())
                                if(isiulang2 == '1'): isiulang_kartu()
                    else: return()
                    #Pembayaran Berhasil
        if(ketemu == False):
        #Pembayaran Gagal
            print("Mohon maaf kode kartu anda tidak teregistrasi.")
            print("Mohon registrasi terlebih dahulu.")
            print("Terima Kasih")
            input()
            return bayar(X)     
    else:
        os.system('cls')
        return bayar(X)

def masukparkir():
    print('Silahkan pilih kendaraan :')
    print('1. Kendaraan roda dua         2. Kendaraan roda empat')
    print('3. Kendaraan lainnya')
    pilihan = (input('Pilihan : '))
    os.system('cls')
    plat = ''
    if pilihan == '1':
        plat = input("Masukkan nomor plat : ")
        plat = 'M' + ''.join(plat)
    elif pilihan == '2':
        plat = input("Masukkan nomor plat : ")
        plat = 'C' + ''.join(plat)
    elif pilihan == '3':
        plat = input("Masukkan nomor plat : ")
        plat = 'B' + ''.join(plat)
    else:
        os.system('cls')
        return masukparkir()

    waktu = datetime.datetime.now()
    Y = waktu.strftime('%d%H%M%S')
    kode = plat + Y
    print('Kode parkir anda adalah : ')
    print(kode)
    print('Silahkan masuk !')
    input()
    os.system('cls')
    return(kode)

def keluarparkir(sebutsesuatu):
    print('Masukkan kode tiket : ')
    simpan = input()
    i = 0
    os.system('cls')
    while i < len(sebutsesuatu):
        if simpan == sebutsesuatu[i]:
            bayar(simpan)
            waktusekarang = datetime.datetime.now()
            Z = waktusekarang.strftime('%H%M%S')
            print('Kendaraan dengan nomor plat ' + str(sebutsesuatu[i][1:len(sebutsesuatu[i])-8]) )
            
            print('Masuk pada pukul ' + str(sebutsesuatu[i][-6:-4]) +':' + str(sebutsesuatu[i][-4:-2]) +
                  ':' + str(sebutsesuatu[i][-2]+sebutsesuatu[i][-1]))
            print('Kendaraan keluar pada pukul ' + Z[0:2] +':' + Z[2:4] + ':' + Z[4:6])
            print('Silahkan keluar, ANDA MEREPOTKAN SAYA!')
            input()
            sebutsesuatu.pop(i)
            return()
        else :
            i = i+1

    if i == len(sebutsesuatu):
        print("Tiket parkir salah")
        input()


daftartiketparkir = []

#Saat kendaraan masuk parkir
waktusek = datetime.datetime.now()
Z = waktusek.strftime('%H')

if(int(Z) >= int("07") and int(Z) <= int("22")):
    print("----------------------------------------------")
    print("Selamat Datang di Program Parkir")
    print("Semoga program ini dapat membantu anda.")
    flag = True
    while(flag):
        waktusek = datetime.datetime.now()
        Z = waktusek.strftime('%H')
        print ('Silahkan ketik 1 untuk kendaraan masuk dan ketik 2 untuk kendaraan keluar:')
        pilihan = (input('Pilihan anda: '))
        if(pilihan == '1'):
            os.system('cls')
            test=masukparkir()
            daftartiketparkir.append(test)
            
        elif(pilihan == '2'): 
            keluarparkir(daftartiketparkir)
            os.system('cls')
        if(int(Z) == int("22")): flag = False
    if(flag == False): print ('Tempat parkir sudah tutup')
elif(int(Z) > int("22")): print('Tempat parkir sudah tutup')
else: print('Tempat parkir belum buka')
