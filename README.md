# MINI PROJECT 1 DASAR-DASAR PEMROGRAMAN 2025

Nama : Alisya Octa Noor Ghina\
NIM : 2509116017\
Project : Sistem Informasi Nilai Siswa Kelas B SMAN 2 BERAU

**1. FLOWCHART**\
<img width="415" height="491" alt="Screenshot (167)" src="https://github.com/user-attachments/assets/73d4fd49-0355-45ba-9f65-755a4ad9e34b" />\
**Penjelasan Flowchart**
1) Flowchart dimulai dengan start
2) Lalu menampilkan menu pilihan
3) Lalu kita diminta untuk menginput pilihan
4) Pilih menu 1?
   - Jika Iya, akan menampilkan pilihan mata pelajaran
   - Jika Tidak, Pilih menu 2?
     - Jika Iya, lanjut ke halaman 2
     - Jika Tidak, Pilih menu 3?
       - Jika Iya, lanjut ke halaman 2
       - Jika Tidak, Pilih menu 4?
         - Jika Iya, lanjut ke halaman 3
         - Jika Tidak, akan menampilkan "Menu Tidak Valid"
5) Input mata pelajaran
6) Pilih Mata pelajaran 1?
   - Jika Iya, akan menampilkan pilihan metode pencarian
   - Jika Tidak, Pilih Mata pelajaran 2?
     - Jika Iya, akan menampilkan metode pencarian
     - Jika Tidak, Pilih Mata Pelajaran 3?
       - Jika Iya, akan menampilkan metode pencarian
       - Jika Tidak, akan menampilkan "Mata Pelajaran Tidak Valid"
7) Input metode pencarian
8) Pilih Metode 1?
   - Jika Iya, Input nama siswa
   - Jika Tidak, pilih metode 2?
     - Jika Iya, Input Nomor Absen siswa
     - Jika Tidak, akan menampilkan "Metode Tidak Valid"
9) Menampilkan nilai
10) End
   


<img width="543" height="492" alt="Screenshot (165)" src="https://github.com/user-attachments/assets/1717acc0-7b34-4bd8-9ef1-18a64902ea98" />\
**Penjelasan Flowchart**
1. Flowchart halaman 2
2. Pilih menu 2?
   - Jika Iya
3. Input Nama siswa
4. Input Nomor Absen Siswa
5. Input Nilai Matematika
6. Input Nilai Bahasa Indonesia
7. Input Nilai Bahasa Inggris
8. Menampilkan hasil penambahahan data siswa
9. End

1. Jika Tidak memilih menu 2, Pilih menu 3?
2. Jika Memilih Menu 3
3. Akan menampilkan pilihan mata pelajaran
4. Input pilihan
5. Pilih Mata Pelajaran 1?
   - Jika Iya, input nomor absen siswa
6. Input nilai baru
7. Akan menampilkan nilai Matematika yang sudah diubah
8. End
   - Jika Tidak memilih mata pelajaran 1, Pilih mata pelajaran 2?
   - Jika Iya, input nomor absen siswa
9. Input nilai baru
10. Akan menampilkan nilai Bahasa Indonesia yang sudah diubah
11. End
    - Jika Tidak memilih mata pelajaran 2, Pilih mata pelajaran 3?
    - Jika Iya, input nomor absen siswa
12. Input nilai baru
13. Akan menampilkan nilai Bahasa Indonesia yang sudah diubah
14. End
    - Jika Tidak memilih mata pelajaran 3, akan menampilkan "Mata Pelajaran Tidak Valid"
15. End
    
<img width="523" height="482" alt="Screenshot (166)" src="https://github.com/user-attachments/assets/2c8e8029-366b-4da9-8d6a-0ac68c495aee" />\
**Penjelasan Flowchart**
1. Flowchart halaman 3
2. Pilih menu 4?
   - Jika Tidak, akan menampilkan "Menu Tidak Valid"
   - End
   - Jika Iya
4. Akan menampilkan pilihan data siswa
5. Input pilihan
6. Pilih data 1?
   - Jika Iya
7. Input Indeks list siswa
8. Akan menampilkan list siswa setelah dihapus
9. Akan menampilkan nama siswa yang dihapus
10. End
    - Jika Tidak, Pilih data 2?
    - Jika Iya
11. Input Indeks list nomor absen
12. Akan menampilkan list nomot absen setelah dihapus
13. Akan menampilkan nomor absen yang dihapus
14. End
    - Jika Tidak memilih data 2, Pilih data 3?
    - Jika Tidak, akan menampilkan "Pilihan Data Tidak Valid"
    - End
    - Jika Iya
15. Menampilkan Pilihan Mata Pelajaran
15. Input Pilihan
16. Pilih Mata Pelajaran 1?
    - Jika Iya
17. Input Indeks list nilai Matematika
18. Akan menampilkan list nilai Matematika setelah dihapus
19. Akan menampilkan nilai Matematika yang dihapus
20. End
    - Jika Tidak memilih mata pelajaran 1, Pilih mata pelajaran 2?
    - Jika Iya
21. Input Indeks list nilai Bahasa Indonesia
22. Akan menampilkan list nilai Bahasa Indonesia setelah dihapus
23. Akan menampilkan nilai Bahasa indonesia yang dihapus
24. End
    - Jika Tidak memilih mata pelajaran 2, Pilih mata pelajaran 3?
    - Jika Tidak, akan menampilkan "Pilihan Mata Pelajaran Tidak Valid"
    - Jika Iya
25. Input Indeks list nilai Bahasa Inggris
18. Akan menampilkan list nilai Bahasa Inggris setelah dihapus
19. Akan menampilkan nilai Bahasa Inggris yang dihapus
20. End


**2. KODE PROGRAM**\
Kode Program : [Mini Project 1.py](https://github.com/user-attachments/files/22309756/Mini.Project.1.py)


<img width="590" height="377" alt="Screenshot (169)" src="https://github.com/user-attachments/assets/1554e394-61e1-43a6-98c2-683fd3bcdb0c" />\
**Penjelasan**\
_List_Mahasiswa_ berisikan daftar nama siswa/i kelas B.\
_No_Absen_ berisikan daftar absen siswa/i kelas B secara urut.\
_Nilai_MTK_ brisikan daftar nilai Matematika siswa/i kelas B secara urut.\
_Nilai_BINDO_ brisikan daftar nilai Bahasa Indonesia siswa/i kelas B secara urut.\
_Nilai_BING_ brisikan daftar nilai Bahasa Inggris siswa/i kelas B secara urut.\
_List_Mapel_ berisikan daftar mata pelajaran yang dinilai.\
Bagian _Tampilan Awal_ berisi Program yang akan menampilkan judul Sistem Informasi Nilai Siswa Kleas B SMAN 2 BERAU dan menu pilihan yang bisa dipilih oleh pengguna. Menu ini nantinya akan digunakan untuk mengakses fungsi-fungsi yang mengelola data siswa dan nilai mereka, seperti menampilkan nilai, menambah siswa baru, mengubah nilai siswa, atau menghapus data siswa.

<img width="640" height="438" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/792a7d03-5db0-4bfd-85c5-ad81fcd9fb8c" />\
**Penjelasan**\
Pada _Menu = int(input("\nPilih Menu (Angka) : "))_\
Program akan meminta pengguna memasukkan angka untuk memilih menu yang ingin dijalankan.\
Pada _if Menu == 1 :_\
Jika pengguna memilih menu 1 (Melihat Nilai Siswa), maka program akan menampilkan daftar mata pelajaran yang tersedia untuk dipilih.\
Pada _Pilih_Mapel = int(input("\nPilih Mata Pelajaran (Angka) : "))_
Program meminta pengguna memasukkan angka untuk memilih mata pelajaran yang ingin dilihat nilainya.\
Berdasarkan input pengguna, program akan menentukan mata pelajaran yang dipilih dan mengambil daftar nilai yang sesuai.\
Jika memilih 1, maka mata pelajaran adalah "Matematika" dan nilai yang diambil adalah Nilai_MTK.\
Jika memilih 2, maka mata pelajaran adalah "Bahasa Indonesia" dan nilai yang diambil adalah Nilai_BINDO.\
Jika memilih 3, maka mata pelajaran adalah "Bahasa Inggris" dan nilai yang diambil adalah Nilai_BING.\
Pada _else : print("\nMata Pelajaran Tidak Valid!")_\
Jika pengguna memasukkan angka selain 1, 2, atau 3, program akan menampilkan "Mata Pelajaran Tidak Valid!" dan menghentikan program dengan exit().

<img width="1048" height="495" alt="Screenshot (143)" src="https://github.com/user-attachments/assets/50e2ff4f-e7be-4b69-a7b0-0fce12455816" />\
**Penjelasan**\
Pada _Metode = input("\nCari Nilai Berdasarkan Nama Siswa (1) atau Nomor Absen (2)? ")_\
Program meminta pengguna memilih metode pencarian nilai siswa, apakah berdasarkan nama siswa (input "1") atau nomor absen (input "2").\
Pada _if Metode == "1" :_ dan _Cari_Nama = input("\nMasukkan Nama Siswa (Kapital) : ")_\
Jika pengguna memilih "1", program akan meminta pengguna memasukkan nama siswa yang ingin dicari nilainya.\
Program akan membandingkan input nama siswa _(Cari_Nama)_ dengan setiap nama dalam list _List_Siswa_ menggunakan beberapa kondisi _if-elif-else_\
Jika nama yang dimasukkan cocok dengan salah satu nama di list, program akan menyimpan indeks siswa tersebut ke variabel _indeks_siswa_.\
Kemudian program menampilkan nilai siswa tersebut untuk mata pelajaran yang sudah dipilih sebelumnya _Mapel_Terpilih_, dengan mengambil nilai dari list nilai yang sesuai _Nilai_Terpilih[indeks_siswa]_.\
Jika nama yang dimasukkan tidak cocok dengan salah satu nama di list atau salah pengetikan, program akan menampilkan "Nama Siswa Tidak Valid! Harus Menggunakan Huruf Kapital."

<img width="466" height="426" alt="Screenshot (151)" src="https://github.com/user-attachments/assets/06f20932-67f0-4db2-bc52-6f3fde78b316" />\
**OUTPUT MENU 1 (MELIHAT NILAI) METODE 1**

<img width="1035" height="462" alt="Screenshot (170)" src="https://github.com/user-attachments/assets/8b612a42-e137-4ee2-b491-31dea2b6e223" />\
**Penjelasan**\
Pada _elif Metode == "2" :_\
Jika pengguna memilih "2", maka program akan melakukan pencarian nilai siswa berdasarkan nomor absen.\
Paada _Cari_Absen = int(input("\nMasukkan Nomor Absen Siswa (Angka) : "))_
Program meminta pengguna untuk memasukkan nomor absen siswa dalam bentuk angka.\
Kemudian, program akan membandingkan nilai input _Cari_Absen_ dengan isi list _No_Absen_ menggunakan beberapa kondisi _if-elif-else_.\
Jika nomor absen yang dimasukkan cocok dengan salah satu nomor absen di list _No_Absen_, program akan menyimpan indeks nomor absen tersebut ke variabel _indeks_absen_.\
Kemudian program menampilkan nilai siswa tersebut untuk mata pelajaran yang sudah dipilih sebelumnya _Mapel_Terpilih_, dengan mengambil nilai dari list nilai yang sesuai _Nilai_Terpilih[indeks_absen]_.\
Jika nomor absen yang dimasukkan tidak cocok dengan salah satu nomor absen di list atau salah pengetikan, program akan menampilkan "NNomor Absen Siswa Tidak Ditemukan."\
Pada _else : print("\nMetode Tidak Valid!")_\
Pesan seperti diatas akan muncul jika pengguna memilih selain "1" atau "2" saat memilih metode.

<img width="469" height="420" alt="Screenshot (152)" src="https://github.com/user-attachments/assets/ce1838d3-cd12-4c07-82a7-4551bf13d7a1" />\
**OUTPUT MENU 1 (MELIHAT NILAI) METODE 2**


<img width="588" height="439" alt="Screenshot (145)" src="https://github.com/user-attachments/assets/10392583-fd02-462f-af3f-e242fbb47063" />\
**Penjelasan**

<img width="680" height="415" alt="Screenshot (153)" src="https://github.com/user-attachments/assets/2f663da8-8a03-422a-a8d2-d5be2d38bb05" />\
**OUTPUT MENU 2 (MENAMBAH DATA)**

<img width="514" height="311" alt="Screenshot (150)" src="https://github.com/user-attachments/assets/f7ecd8c9-4ac9-455e-a346-2154d07d3b74" />\
**Penjelasan**

<img width="489" height="378" alt="Screenshot (147)" src="https://github.com/user-attachments/assets/3ed10808-58dc-41f0-bd78-f8ec61cd3ce5" />\
**Penjelasan**

<img width="455" height="381" alt="Screenshot (154)" src="https://github.com/user-attachments/assets/afe90ede-74f0-48a4-b469-6948399b668b" />\
**OUTPUT MENU 3 (MENGUBAH NILAI)**

<img width="586" height="344" alt="Screenshot (148)" src="https://github.com/user-attachments/assets/93ae2aae-f6f5-489b-8dc1-aef64fa70ca9" />\
**Penjelasan**

<img width="524" height="355" alt="Screenshot (155)" src="https://github.com/user-attachments/assets/8095653f-9ea5-4dbe-b650-4a765b54742a" />\
**OUTPUT MENU 4 (MENGHAPUS DATA) KONDISI 1**

<img width="458" height="342" alt="Screenshot (156)" src="https://github.com/user-attachments/assets/e72556f3-8592-4ea1-96d0-cd397b0119f2" />\
**OUTPUT MENU 4 (MENGHAPUS DATA) KONDISI 2**


<img width="671" height="564" alt="Screenshot (162)" src="https://github.com/user-attachments/assets/229ed56c-4819-430a-853c-fabbf0ca0aec" />\
**Penjelasan**

<img width="478" height="442" alt="Screenshot (158)" src="https://github.com/user-attachments/assets/6ddb88f6-d4f2-4e19-bdc1-0752105fa845" />\
**OUTPUT MENU 4 (MENGHAPUS DATA) KONDISI 3**
