# ⚠️ WARNING ⚠️
## PERINGATAN: HARAP BACA BAGIAN INI TERLEBIH DAHULU SEBELUM MENGGUNAKAN PROGRAM INI!

### JANGAN LAKUKAN SALAH SATUPUN DARI YANG DIBAWAH INI AGAR PROGRAM INI TIDAK MENGALAMI NOT RESPONDING!
**1. Membuka window lain saat window visualisasi sedang berjalan** <br>
** Menutup/Meminimize window visualisasi saat visualisasi sedang berlangsung** <br>
<br>
<font color="green" size = "4"> Disarankan untuk menekan tombol close <b>SETELAH PROSES VISUALISASI KURVA BEZIER SELESAI. </b>Akan ada jeda waktu selama 10 detik setelah visualisasi kurva bezier selesai bagi pengguna untuk menekan tombol close. Jika tombol close tidak ditekan selama jeda waktu tersebut, <b>proses visualisasi akan diulang dari awal kembali.</b>  </font><br>
<font color="green" size = "4">Jika Anda tidak melakukan kedua hal di atas, proses visualisasi tetap akan berfungsi sebagaimana mestinya.</font><br>
# Deskripsi Singkat
Program ini adalah sebuah program yang bertujuan untuk melakukan simulasi kurva bezier dengan **n buah** control point.

# Requirements
1. ```Python 3.10.6```
2. ```tkinter 0.1.0```
3. ```pygame 2.5.2```
4. ```pyinstaller 6.5.0```

# Cara Mengompilasi Program
1. Buka Terminal/Powershell/Command Prompt di folder src repository ini.
2. Jika Anda membuka Terminal/Powershell/Command Prompt bukan di folder src repository ini, salin direktori folder src repository ini dari file explorer dan ketik ``` cd "salin direktori folder src di sini" ``` pada Terminal/Powershell/Command Prompt. ***CATATAN: Tanda petik dua wajib diketik di sebelah kiri dan sebelah kanan direktori folder src yang Anda salin***
3. Ketik ```python app_init.py``` di Terminal/Powershell/Command Prompt.
4. Tunggu sampai program selesai terkompilasi dan window GUI akan ditampilkan

# Cara Membuild Program
1. Buka Terminal/Powershell/Command Prompt di folder src repository ini.
2. Jika Anda membuka Terminal/Powershell/Command Prompt bukan di folder src repository ini, salin direktori folder src repository ini dari file explorer dan ketik ``` cd "salin direktori folder src di sini" ``` pada Terminal/Powershell/Command Prompt. ***CATATAN: Tanda petik dua wajib diketik di sebelah kiri dan sebelah kanan direktori folder src yang Anda salin***
3. Ketik ```pyinstaller --onefile --noconsole -i "Directory ke file BezierCurveIcon.ico dengan tanda petik (BezierCurveIcon.ico terletak di dalam folder src di repository ini)" app_init.py --name "Bezier Curve Simulation" --distpath "Directory ke folder bin di repository ini"``` di Terminal/Powershell/Command Prompt.
4. Tunggu sampai proses building selesai dan akan ada file executable yang tersimpan di dalam folder bin dengan nama ```Bezier Curve Simulation.exe```
# Cara Menggunakan Program
Berikut adalah video tata cara penggunaan program ini.

# Keterangan Warna Di Visualizer
1. Titik berwarna <font color = "blue" size = 3>**biru**</font> di dalam visualizer program ini adalah **Control Point** dan garis berwarna <font color = "blue" size = 3>**biru**</font> adalah **garis penghubung control point**.
2. Titik berwarna <font color = "green" size = 3>**hijau**</font> di dalam visualizer program ini adalah **Titik Tengah/Midpoint** dan garis berwarna <font color = "green" size = 3>**hijau**</font> adalah **garis penghubung Midpoint** *(Hanya akan muncul jika pengguna memilih metode Divide And Conquer)* 
3. Titik berwarna <font color = "red" size = 3>**merah**</font> adalah titik yang terletak dalam kurva bezier yang terbentuk dan garis berwarna <font color = "red" size = 3>**merah**</font> adalah **kurva bezier yang terbentuk**
# Tentang Pembuat Program
| Nama          | NIM    | Kelas Strategi Algoritma|
| --------------|--------| ----|
|Akbar Al Fattah|13522036| K-02|
|Devinzen       |13522064| K-02|
# Check List Program
| No | Poin | Ya | Tidak |
| --- | --- | --- | --- |
| 1 | Program berhasil dijalankan | V | |
| 2 | Program dapat melakukan visualisasi kurva Bézier | V | |
| 3 | Solusi yang diberikan program optimal | V | |
| 4 | [Bonus] Program dapat membuat kurva untuk n titik kontrol | V | |
| 5 |  [Bonus] Program dapat melakukan visualisasi proses pembuatan kurva | V | |
