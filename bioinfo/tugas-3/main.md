
untuk mengikuti proses ini diperlukan aplikasi Phylip yang dapat diunduh di https://evolution.genetics.washington.edu/phylip.html dan figtree (untuk menampilkan pohon) yang dapat diunduh di http://tree.bio.ed.ac.uk/software/figtree/. Untuk menggunakan figTree, perlu diinstall java terlebih dahulu pada laman https://www.java.com/en/. Setelah proses penginstallan akan terdapat tampilan seperti berikut:

Selain itu, data sequence allignment pada prosedur berikut dapat diunduh pada https://drive.google.com/drive/folders/1C_-KpkBNbFCVOMPCBz8DL-WnHV9puTLR?usp=sharing 

untuk menghasilkan pohon NJ menggunakan program Neighbor.exe dari paket Phylip untuk
alignmen primata (file primates_5.phy: alignment dalam format Phylip berurutan),
diperlukan file input dengan jarak evolusi berpasangan. Oleh karena itu, sebelum
memulai program neighbor-joining, pertama-tama hitung matriks jarak menggunakan
program DNAdist.exe. Gunakan model F84 dan rasio transisi / transversi empiris 2. 

lakukan prosedur berikut:
1. buka program DNAdist.exe pada phylip
2. kemungkinan besar akan muncul error seperti berikut: dnadist.exe: can't find input file "infile"
Please enter a new file name>
3. drag and drop file primates_5.phy ke dalam tampilan cmdnya
4. kemudian akan muncul tampilan seperti pada gambar berikut:
5. by default, kriteria perhitungan jarak menggunakan model F84 dan rasio transisi/transversi empiris 2. yang perlu dilakukan adalah menekan "Y" untuk mengkonfirmasi
6. kemudian akan ada file outfile pada folder yang sama dengan DNAdist.exe
7. ubah nama file outfile menjadi infile
8. buka program neighbor.exe pada phylip
9. by default, algoritma yang akan dijalankan adalah neighbor-joining. tekan "Y" untuk mengkonfirmasi.
10. kemudian akan muncul dua file output, yaitu outtree dan outfile. outtree berisi pohon yang dihasilkan yang dapat dibuka dengan figtree. , sedangkan outfile merupakan tampilan tree dan jarak yang dapat dibuka dengan txt editor
11. Buka aplikasi figtree dan buka file outtree yang telah dihasilkan
12. hasilnya akan seperti berikut:
13. Perlu dicatat bahwa NJ tree adalah algorithma untuk menghasilkan pohon yang tidak membutuhkan root. Oleh karena itu, ubah tampilan menjadi unrooted tree dengan klik tombol pada bagian layout.



Untuk mengikuti proses ini, diperlukan aplikasi Phylip yang dapat diunduh dari situs web berikut: https://evolution.genetics.washington.edu/phylip.html, dan aplikasi FigTree (untuk menampilkan pohon) yang dapat diunduh dari http://tree.bio.ed.ac.uk/software/figtree/. Untuk menggunakan FigTree, perlu diinstalasi Java terlebih dahulu dari https://www.java.com/en/ . Setelah proses penginstalan selesai, akan muncul tampilan seperti yang terlihat di bawah ini pada folder download.



Selain itu, data sequence alignment yang diperlukan untuk prosedur ini dapat diunduh dari [https://drive.google.com/drive/folders/1C_-KpkBNbFCVOMPCBz8DL-WnHV9puTLR?usp=sharing](https://drive.google.com/drive/folders/1C_-KpkBNbFCVOMPCBz8DL-WnHV9puTLR?usp=sharing).

Untuk menghasilkan pohon Neighbor-Joining (NJ) menggunakan program Neighbor.exe dari paket Phylip untuk alignment primata (file primates_5.phy: data alignment dalam format Phylip), diperlukan file input dengan jarak evolusi antar sequence yang sudah diallign. Oleh karena itu, sebelum memulai program Neighbor-Joining, pertama-tama hitung matriks jarak menggunakan program DNAdist.exe. Gunakan model F84 dan rasio transisi/transversi empiris 2.

Berikut adalah langkah-langkah yang perlu diikuti:

1. Buka program DNAdist.exe dalam paket Phylip.

2. Kemungkinan besar akan muncul pesan error seperti berikut: "dnadist.exe: can't find input file "infile". Please enter a new file name."

3. Tarik dan lepaskan file primates_5.phy ke dalam jendela perintah (cmd).

4. Kemudian akan muncul tampilan seperti yang ditunjukkan dalam gambar berikut:

![DNAdist.exe](insert_gambar_dnadist_exe.png)

5. Secara default, kriteria perhitungan jarak menggunakan model F84 dan rasio transisi/transversi empiris 2. Tekan "Y" untuk mengkonfirmasi.

6. Kemudian akan ada file outfile yang akan terletak dalam folder yang sama dengan DNAdist.exe.

7. Ubah nama file outfile menjadi "infile".

8. Buka program neighbor.exe dalam paket Phylip.

9. Secara default, algoritma yang akan dijalankan adalah Neighbor-Joining. Tekan "Y" untuk mengkonfirmasi.

10. Kemudian akan muncul dua file output, yaitu outtree dan outfile. Outtree berisi pohon yang dihasilkan yang dapat dibuka dengan FigTree, sedangkan outfile berisi tampilan pohon dan jarak yang dapat dibuka dengan editor teks.

11. Buka aplikasi FigTree dan buka file outtree yang telah dihasilkan.

12. Hasilnya akan terlihat seperti berikut:

![Hasil Pohon](insert_gambar_hasil_pohon.png)

    13. Perlu dicatat bahwa pohon NJ adalah algoritma untuk menghasilkan pohon yang tidak memerlukan root. Oleh karena itu, Anda dapat mengubah tampilan menjadi pohon tanpa root dengan mengklik tombol yang sesuai pada bagian tata letak (layout) aplikasi FigTree.