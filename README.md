# MINI PROJECT 1 DASAR-DASAR PEMROGRAMAN 2025

Nama : Alisya Octa Noor Ghina\
NIM : 2509116017\
Project : Sistem Informasi Nilai Siswa Kelas B SMAN 2 BERAU

**1. FLOWCHART**\
![Mini Project 1-Halaman-1](https://github.com/user-attachments/assets/35fbe7b5-1e8e-488e-8245-5f51f842bbe4)

![Mini Project 1-Halaman-2](https://github.com/user-attachments/assets/2b65978b-aaf5-47f0-bbf7-07a1038b415b)

![Mini Project 1-Halaman-3](https://github.com/user-attachments/assets/e7b778f6-e2d8-40ad-896b-7010cd06d566)


**2. KODE PROGRAM**\
Kode Program : [Mini Project 1.py](https://github.com/user-attachments/files/22311402/Mini.Project.1.py)


**3. PENJELASAN ALUR PROGRAM DAN OUTPUT**\
<img width="590" height="377" alt="Screenshot (169)" src="https://github.com/user-attachments/assets/1554e394-61e1-43a6-98c2-683fd3bcdb0c" />

<img width="474" height="230" alt="Screenshot (159)" src="https://github.com/user-attachments/assets/da77330e-34d3-449c-b978-8798f13620b5" />\
_**Output Jika Tidak Memilih Menu 1, 2, 3, atau 4**_

**Penjelasan**\
Bagian _Tampilan Awal_ berisi Program yang akan menampilkan judul Sistem Informasi Nilai Siswa Kleas B SMAN 2 BERAU dan menu pilihan yang bisa dipilih oleh pengguna. Menu ini nantinya akan digunakan untuk mengakses fungsi-fungsi yang mengelola data siswa dan nilai mereka, seperti menampilkan nilai, menambah siswa baru, mengubah nilai siswa, atau menghapus data siswa.\
Jika pengguna memasukkan angka selain 1, 2, 3, atau 4,  program akan menampilkan "Menu Tidak Valid!" dan menghentikan program.

<img width="640" height="438" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/792a7d03-5db0-4bfd-85c5-ad81fcd9fb8c" />


<img width="454" height="346" alt="Screenshot (160)" src="https://github.com/user-attachments/assets/6f0f31b5-0e33-4c81-aa75-41906d505235" />\
_**Output Jika Tidak Memilih Mata Pelajaran 1, 2, ataupun 3**_

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


<img width="1048" height="495" alt="Screenshot (143)" src="https://github.com/user-attachments/assets/50e2ff4f-e7be-4b69-a7b0-0fce12455816" />

<img width="466" height="426" alt="Screenshot (151)" src="https://github.com/user-attachments/assets/06f20932-67f0-4db2-bc52-6f3fde78b316" />\
_**Output Menu 1 (Melihat Nilai) Menggunakan Metode 1 (Nama Siswa)**_

**Penjelasan**\
Pada _Metode = input("\nCari Nilai Berdasarkan Nama Siswa (1) atau Nomor Absen (2)? ")_\
Program meminta pengguna memilih metode pencarian nilai siswa, apakah berdasarkan nama siswa (input "1") atau nomor absen (input "2").\
Pada _if Metode == "1" :_ dan _Cari_Nama = input("\nMasukkan Nama Siswa (Kapital) : ")_\
Jika pengguna memilih "1", program akan meminta pengguna memasukkan nama siswa yang ingin dicari nilainya.\
Program akan membandingkan input nama siswa _(Cari_Nama)_ dengan setiap nama dalam list _List_Siswa_ menggunakan beberapa kondisi _if-elif-else_\
Jika nama yang dimasukkan cocok dengan salah satu nama di list, program akan menyimpan indeks siswa tersebut ke variabel _indeks_siswa_.\
Kemudian program menampilkan nilai siswa tersebut untuk mata pelajaran yang sudah dipilih sebelumnya _Mapel_Terpilih_, dengan mengambil nilai dari list nilai yang sesuai _Nilai_Terpilih[indeks_siswa]_.\
Jika nama yang dimasukkan tidak cocok dengan salah satu nama di list atau salah pengetikan, program akan menampilkan "Nama Siswa Tidak Valid! Harus Menggunakan Huruf Kapital."

<img width="1035" height="462" alt="Screenshot (170)" src="https://github.com/user-attachments/assets/8b612a42-e137-4ee2-b491-31dea2b6e223" />

<img width="469" height="420" alt="Screenshot (152)" src="https://github.com/user-attachments/assets/ce1838d3-cd12-4c07-82a7-4551bf13d7a1" />\
_**Output Menu 1 (Melihat Nilai) Menggunakan Metode 2 (Nomor Absen)**_

<img width="458" height="383" alt="Screenshot (177)" src="https://github.com/user-attachments/assets/07233aa5-eae9-449e-9357-6b21a196baae" />\
_**Output Jika Tidak Memilih Metode 1 atau 2**_

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

<img width="588" height="439" alt="Screenshot (145)" src="https://github.com/user-attachments/assets/10392583-fd02-462f-af3f-e242fbb47063" />

<img width="680" height="415" alt="Screenshot (153)" src="https://github.com/user-attachments/assets/2f663da8-8a03-422a-a8d2-d5be2d38bb05" />\
_**Output Menu 2 (Menambah Data)**_

**Penjelasan**\
Jika pengguna memilih menu nomor 2 (Menambah Data Siswa), maka program akan menampilkan perintah untuk menginput Nama siswa, Nomor absen, Nilai Matematika, Nilai Bahasa Indonesia dan Nilai Bahasa Inggris.\
Semua input ini akan disimpan ke dalam variabel sementara: Tambah_Nama, Tambah_Absen, Tambah_Nilai_MTK, Tambah_Nilai_BINDO, Tambah_Nilai_BING.\
Pada bagian _append()_ Program akan menambahkan data baru ke dalam masing-masing list data dan akan disimpan di akhir list tanpa menghapus data lama.\
Setelah data berhasil ditambahkan, program menampilkan pesan konfirmasi dan seluruh isi list terbaru.\


<img width="514" height="311" alt="Screenshot (150)" src="https://github.com/user-attachments/assets/f7ecd8c9-4ac9-455e-a346-2154d07d3b74" />

<img width="470" height="325" alt="Screenshot (178)" src="https://github.com/user-attachments/assets/7b66d587-4f27-42b1-bb80-6d5380a02635" />\
_**Output Jika Memilih di luar angka 1, 2, ataupun 3**_

**Penjelasan**\
Pada _elif Menu == 3 :_
Jika pengguna memilih menu nomor 3 (Mengubah Nilai Siswa), maka program akan menampilkan daftar mata pelajaran.\
Pengguna diminta memilih mata pelajaran mana yang nilainya ingin diubah.\
Jika pilih 1, maka variabel Nilai_Terpilih menunjuk ke list Nilai Matematika.\
Jika pilih 2, maka Nilai_Terpilih menunjuk ke list Nilai Bahasa Indonesia.\
Jika pilih 3, maka Nilai_Terpilih menunjuk ke list Nilai Bahasa Inggris.\
Jika pilih di luar angka 1–3, program menampilkan "Mapel tidak valid!" dan berhenti.

<img width="497" height="389" alt="Screenshot (172)" src="https://github.com/user-attachments/assets/7952b141-43eb-407f-924c-59ccdae17850" />

<img width="455" height="381" alt="Screenshot (154)" src="https://github.com/user-attachments/assets/afe90ede-74f0-48a4-b469-6948399b668b" />\
_**Output Menu 3 (Mengubah Nilai)**_

<img width="471" height="346" alt="Screenshot (179)" src="https://github.com/user-attachments/assets/a07d9355-9d97-4146-b30e-024735b26ab0" />\
_**Output Jika Memilih Menu 3 Tetapi tidak memasukkan Absen yang tersedia di list**_

**Penjelasan**\
Pada _No_Absen = int(input("\nMasukkan Nomor Absen Siswa: "))_
Pengguna diminta memasukkan nomor absen siswa yang nilainya akan diubah.\
Kemudian, program akan membandingkan nilai input _No_Absen_ dengan isi list _No_Absen_ menggunakan beberapa kondisi _if-elif-else_.\
Contohnya : Jika memasukkan nomor absen 1, program akan mengubah nilai di Nilai_Terpilih[0].\
Setelah diganti, program menampilkan "Nilai Berhasil Diperbarui".\
Jika nilai input _No_Absen_ dengan isi list _No_Absen_ tidak cocok, program akan menampilkan "Absen Tidak Ditemukan".


<img width="586" height="344" alt="Screenshot (148)" src="https://github.com/user-attachments/assets/93ae2aae-f6f5-489b-8dc1-aef64fa70ca9" />

<img width="524" height="355" alt="Screenshot (155)" src="https://github.com/user-attachments/assets/8095653f-9ea5-4dbe-b650-4a765b54742a" />\
_**Output Menu 4 (Menghapus Data) Kondisi 1 (Menghapus Nama)**_

**Penjelasan**
Pada _elif Menu == 4 :_\
Jika pengguna memilih menu nomor 4 (Menghapus Data), maka program akan menampilkan sub-menu pilihan data yang ingin dihapus.\
Pengguna dapat memilih : Menghapus nama siswa dari List_Siswa, Menghapus nomor absen siswa dari No_Absen, dan Menghapus nilai siswa dari list nilai.\
Jika pengguna memilih sub-menu nomor 1, Program meminta pengguna memasukkan indeks _List_Siswa_. pop(indeks) akan menghapus data pada posisi tertentu di dalam list _List_Siswa_. Data yang terhapus disimpan sementara dalam variabel _Pilih_Menu4_ lalu akan ditampilkan kembali sebagai konfirmasi.

<img width="458" height="342" alt="Screenshot (156)" src="https://github.com/user-attachments/assets/e72556f3-8592-4ea1-96d0-cd397b0119f2" />\
_**Output Menu 4 (Menghapus Data) Kondisi 2 (Menghapus Absen)**_

**Penjelasan**\
Pada _elif Menu == 4 :_\
Jika pengguna memilih menu nomor 4 (Menghapus Data), maka program akan menampilkan sub-menu pilihan data yang ingin dihapus.\
Pengguna dapat memilih : Menghapus nama siswa dari List_Siswa, Menghapus nomor absen siswa dari No_Absen, dan Menghapus nilai siswa dari list nilai.\
Jika pengguna memilih sub-menu nomor 2, Program meminta pengguna memasukkan indeks _No_Absen_. pop(indeks) akan menghapus data pada posisi tertentu di dalam list _No_Absen_. Data yang terhapus disimpan sementara dalam variabel _Pilih_Menu4_ lalu akan ditampilkan kembali sebagai konfirmasi.


<img width="675" height="622" alt="Screenshot (176)" src="https://github.com/user-attachments/assets/ae3fc08c-2153-4e16-b89a-4c7d4810a7fa" />

<img width="478" height="442" alt="Screenshot (158)" src="https://github.com/user-attachments/assets/6ddb88f6-d4f2-4e19-bdc1-0752105fa845" />\
_**Output Menu 4 (Menghapus Data) Kondisi 3 (Menghapus Nilai)**_

**Penjelasan**\
Pada _elif Menu == 4 :_\
Jika pengguna memilih menu nomor 4 (Menghapus Data), maka program akan menampilkan sub-menu pilihan data yang ingin dihapus.\
Pengguna dapat memilih : Menghapus nama siswa dari List_Siswa, Menghapus nomor absen siswa dari No_Absen, dan Menghapus nilai siswa dari list nilai.\
Jika pengguna memilih sub-menu nomor 3, Program akan menampilkan daftar mata pelajaran yang nilainya ingin dihapus.\
Kemudian, pengguna diminta memilih mata pelajaran mana yang nilainya ingin dihapus.
- Jika pengguna memilih mapel nomor 1, Program akan meminta pengguna meemasukkan indeks (posisi siswa) di list Nilai_MTK. pop(indeks) akan menghapus nilai Matematika pada indeks tersebut. Kemudian, program akan menampilkan list terbaru Nilai_MTK dan nilai yang dihapus.
- Jika pengguna memilih mapel nomor 2, Program akan meminta pengguna meemasukkan indeks (posisi siswa) di list Nilai_BINDO. pop(indeks) akan menghapus nilai Matematika pada indeks tersebut. Kemudian, program akan menampilkan list terbaru Nilai_BINDO dan nilai yang dihapus.
- Jika pengguna memilih mapel nomor 3, Program akan meminta pengguna meemasukkan indeks (posisi siswa) di list Nilai_BING. pop(indeks) akan menghapus nilai Matematika pada indeks tersebut. Kemudian, program akan menampilkan list terbaru Nilai_BING dan nilai yang dihapus.

<img width="457" height="431" alt="Screenshot (180)" src="https://github.com/user-attachments/assets/0338ce84-d415-4244-bafe-892daad27b6a" />\
_**Output Jika Memilih Menu 4 Tetapi Memasukkan Mapel Yang Tidak Tersedia**_

**Penjelasan**\
Pada _elif Menu == 4 :_\
Jika pengguna memilih menu nomor 4 (Menghapus Data), maka program akan menampilkan sub-menu pilihan data yang ingin dihapus.\
Pengguna dapat memilih : Menghapus nama siswa dari List_Siswa, Menghapus nomor absen siswa dari No_Absen, dan Menghapus nilai siswa dari list nilai.\
Jika pengguna memasukkan angka selain 1–3, program akan menampilkan "Mata Pelajaran Tidak Valid" dan berhenti.



