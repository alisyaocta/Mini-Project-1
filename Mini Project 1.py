# LIST DATA
List_Siswa = ["ALESSIO","ALISYA","ANINDYA","CLARESTA","GIFARA"]
No_Absen = [1, 2, 3, 4, 5]

# LIST NILAI
Nilai_MTK = [85, 90, 95, 85, 83, 92]
Nilai_BINDO = [85, 84, 90, 80, 83, 84]
Nilai_BING = [88, 89, 92, 81, 84, 89]
Nilai_IPA = [80, 91, 93, 89, 90, 91] 
Nilai_IPS = [90, 90, 91, 85, 87, 89]

# LIST MATA PELAJARAN
List_Mapel = ["Matematika","Bahasa Indonesia","Bahasa Inggris"]

# TAMPILAN AWAL OUTPUT 
print("\n===== Sistem Informasi Nilai Siswa Kelas B SMAN 2 BERAU =====")
print("\nPilih Mata Pelajaran Yang Ingin Anda Lihat Nilainya (Angka) : ")
print("1. Matematika")
print("2. Bahasa Indonesia")
print("3. Bahasa Inggris")

# PILIH MAPEL YANG INGIN DILIHAT NILAINYA
Pilih_Mapel = int(input("\nMasukkan Nomor Mata Pelajaran : "))
if Pilih_Mapel == 1 :
    Mapel_Terpilih = List_Mapel[0]
    Nilai_Terpilih = Nilai_MTK
elif Pilih_Mapel == 2 :
    Mapel_Terpilih = List_Mapel[1]
    Nilai_Terpilih = Nilai_BINDO
elif Pilih_Mapel == 3 :
    Mapel_Terpilih = List_Mapel[2]
    Nilai_Terpilih = Nilai_BING
else : 
    print("\nNomor Mata Pelajaran Tidak Valid!")
    exit()

# MEMILIH METODE PENCARIAN
Metode = input("\nCari Berdasarkan Nama Siswa (1) atau Nomor Absen (2)? ")

# MEMILIH METODE 1
if Metode == "1" :
    Cari_Nama = input("\nMasukkan Nama Siswa (Kapital) : ")
    if Cari_Nama == List_Siswa[0]:
        indeks_siswa = 0
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_siswa]," adalah ",str(Nilai_Terpilih[indeks_siswa])," =====")
    elif Cari_Nama == List_Siswa[1]:
        indeks_siswa = 1
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_siswa]," adalah ",str(Nilai_Terpilih[indeks_siswa])," =====")
    elif Cari_Nama == List_Siswa[2]:
        indeks_siswa = 2
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_siswa]," adalah ",str(Nilai_Terpilih[indeks_siswa])," =====")
    elif Cari_Nama == List_Siswa[3]:
        indeks_siswa = 3
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_siswa]," adalah ",str(Nilai_Terpilih[indeks_siswa])," =====")
    elif Cari_Nama == List_Siswa[4]:
        indeks_siswa = 4
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_siswa]," adalah ",str(Nilai_Terpilih[indeks_siswa])," =====")
    else :
        print("\nNama Siswa Tidak Valid! Harus Menggunakan Huruf Kapital!")
        exit()

# MEMILIH METODE 2
elif Metode == "2" :
    Cari_Absen = int(input("\nMasukkan Nomor Absen Siswa (Angka) : "))
    if Cari_Absen == No_Absen[0]:
        indeks_absen = 0
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_absen]," adalah ",str(Nilai_Terpilih[indeks_absen])," =====")
    elif Cari_Absen == No_Absen[1]:
        indeks_absen = 1
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_absen]," adalah ",str(Nilai_Terpilih[indeks_absen])," =====")
    elif Cari_Absen == No_Absen[2]:
        indeks_absen = 2
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_absen]," adalah ",str(Nilai_Terpilih[indeks_absen])," =====")
    elif Cari_Absen == No_Absen[3]:
        indeks_absen = 3
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_absen]," adalah ",str(Nilai_Terpilih[indeks_absen])," =====")
    elif Cari_Absen == No_Absen[4]:
        indeks_absen = 5
        print("\n===== Nilai ",Mapel_Terpilih," ",List_Siswa[indeks_absen]," adalah ",str(Nilai_Terpilih[indeks_absen])," =====")
    else :
        print("\nNomor Absen Siswa Tidak Ditemukan")

else:
    print("\nMetode Pilihan Tidak Valid!")
    exit()