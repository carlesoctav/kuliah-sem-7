---
marp: true
---
# 2.3.1 Latar Belakang dan Perkembangan Terkini
---

Secara umum Metode berbasis jarak untuk konstruksi pohon filogenetik melibatkan dua tahapan utama: menghitung matriks jarak dan mendapatkan pohon filogenetik dari matriks tersebut.

---
Matriks jarak diharapkan lengkap, artinya semua jarak pasangan antara barisan diketahui. Namun, data yang hilang dapat mempersulit proses ini, dan kemungkinan data yang hilang meningkat dengan jumlah data yang dianalisis.
Data yang hilang dalam filogenetik dapat terjadi karena berbagai alasan, termasuk kegagalan eksperimental, protokol pengumpulan data, pendekatan sampling takson dan gen, serta kelahiran dan kehilangan gen.
Untuk membangun matriks jarak pasangan, barisan diperoleh dan diselaraskan. Ketidakseragaman antara barisan dihitung berdasarkan jumlah posisi yang berbeda dalam selarasan mereka, yang kemudian dikonversi menjadi jarak evolusi.

---

Masalah data yang hilang dalam matriks jarak filogenetik muncul dari karakter yang hilang dalam selarasan barisan, membuatnya sulit untuk menghitung jarak antara barisan dengan data yang hilang. Dalam kehadiran data yang hilang, akurasi pohon filogenetik dapat terpengaruh, sehingga sangat diperlukannya teknik estimasi yang efisien.

---

![](https://lh6.googleusercontent.com/aqdoP-nObAaSZvhLP5uZ4Mo3u8A8nWqK9uCCl_QxO624_7hV4m1B096bEexAYMBO9YrjzpLZrUOote9OndRTGw9Pd8xw9DAZUTMT6YgZTlvC0R3NxetjgSMHQl5_zyqjwTegrD4lvPb4nfzwtSX9KV4)


---

Metode untuk mengatasi data yang hilang dalam matriks jarak filogenetik dapat dikategorikan sebagai metode langsung dan tidak langsung. Metode langsung mencoba untuk menyimpulkan pohon filogenetik secara langsung dari matriks jarak yang tidak lengkap, sementara metode tidak langsung pertama-tama mengimputasi informasi yang hilang dalam matriks dan kemudian membangun pohon. Metode langsung memiliki persyaratan tertentu, seperti berbagi jarak yang diketahui antara elemen-elemen, dan mereka memberlakukan batasan pada aplikasi mereka.

---

Metode tidak langsung, termasuk pendekatan statistik dan pembelajaran mesin, bertujuan untuk mengimputasi jarak yang hilang dan memiliki keunggulan seperti tidak bergantung pada hipotesis jam molekuler. Namun, tantangan seperti persentase data yang hilang yang besar tetap ada.

---

Untuk mengatasi tantangan yang diidentifikasi, penelitian ini memperkenalkan kerangka kerja berbasis ML yang disebut "PhyloMissForest." Kerangka kerja ini menggabungkan algoritma imputasi tak terawasi (unsupervised learning) berbasis random forest, teknik pencarian, dan kriteria filogenetik untuk secara efektif mengimputasi data yang hilang dalam matriks jarak pasangan filogenetik. PhyloMissForest menawarkan solusi yang dapat disesuaikan dan dapat disesuaikan untuk mengatasi data yang hilang dalam skenario filogenetik, menyediakan kerangka kerja yang terpadu untuk berbagai strategi algoritma yang dipandu oleh prinsip-prinsip filogenetik

---


# 2.3.5 Hasil Penelitian
---
Bagian ini membahas evaluasi eksperimental dari kerangka kerja PhyloMissForest yang diusulkan. Metodologi eksperimen melibatkan beberapa langkah:

1. Matriks jarak input yang berasal dari data barisan digunakan.
2. Data yang hilang secara acak diperkenalkan untuk mencapai berbagai persentase (dari 5% hingga 60%).
3. PhyloMissForest diterapkan untuk mengisi entri yang hilang.
4. Pohon filogenetik yang dihasilkan oleh PhyloMissForest dibandingkan dengan pohon referensi yang berasal dari matriks jarak asli.

---

Keberhasilan kerangka kerja dalam memulihkan data asli dan hubungan filogenetik diukur menggunakan metrik Robinson-Foulds (RF). RF digunakan untuk membandingkan dua pohon filogenetik yang tidak berakar (*unrooted*) dengan memeriksa perbedaan dalam pembagian yang diinduksi oleh pada node-nya. Metrik Robinson-Foulds yang dinormalisasi (NRF) digunakan untuk menyatakan persentase perbedaan antara dua pohon, dihitung sebagai skor RF dibagi oleh skor RF maksimum yang mungkin (2N - 6, di mana N adalah jumlah OTUs). Berikut adalah persamaan untuk NRF:
$$
\text { NRF }=\frac{\text { RF }}{2 N-6}
$$
---

kinerja PhyloMissForest dinilai melalui perbandingan dengan dua teknik imputasi filogenetik berbasis machine learning terkemuka *(state-of-the-art)*: faktorisasi matriks dan autoencoder. Evaluasi ini menggunakan tiga dataset:

1. Dataset yang berisi 9 barisan data baculovirus.
2. Dataset asam amino yang terdiri dari 37 barisan fungi xylona heveae.
3. Dataset DNA dengan 55 barisan tanaman hijau.

---

Analisis ini juga melibatkan metodologi statistik untuk membandingkan sampel normalized Robinson-Foulds (NRF) yang dihasilkan oleh metode yang dibandingkan. Pertama, uji Kolmogorov-Smirnov digunakan untuk memeriksa apakah sampel mengikuti distribusi Gaussian. Jika demikian, uji Levene digunakan untuk menguji homogenitas varian. Jika distribusi Gaussian dan homogenitas varian terkonfirmasi, ANOVA digunakan untuk menganalisis signifikansi statistik. Jika tidak, uji Wilcoxon-Mann-Whitney digunakan. Analisis ini dilakukan dengan tingkat kepercayaan 90%.

---

evaluasi komprehensif PhyloMissForest dilakukan dalam konfigurasi bootstrap dan non-bootstrap, membandingkannya dengan dua metode terkemuka (*state-of-the-art*): autoencoder dan faktorisasi matriks. Untuk melakukan evaluasi perbandingan ini, analisis dilakukan di berbagai dataset dengan data yang hilang mulai dari 5% hingga 60%, dengan peningkatan sebesar 5%.

---

Untuk setiap persentase data yang hilang, akan diuji  dengan 10 matriks jarak. hal ini disebabkan kendala eksperimental dan pengaruh komponen stokastik, setiap matriks dijalankan sebanyak 5 kali, dan hasil rata-rata dari 5 percobaan tersebut dihitung. Ini menghasilkan total 50 percobaan untuk setiap persentase data yang hilang. Kami menerapkan prosedur ini pada algoritma random forest dalam kedua konfigurasi dan autoencoder.

---

Namun, dalam kasus faktorisasi matriks, waktu eksekusi yang sangat besar dari pendekatan ini membatasi eksperimen hingga 10 percobaan per persentase data yang hilang. Hasil untuk setiap persentase data yang hilang ditentukan dengan mengambil rata-rata hasil dari 10 matriks yang diuji.

---

# 2.3.5.1 Kasus 9x9 
---


Dalam bagian ini, dilakukan analisis komprehensif pada dataset 9×9, dengan fokus pada hasil NRF (Normalized Robinson-Foulds) yang berasal dari tiga pendekatan berbeda - metode random forest usulkan dan dua teknik terkemuka berbasis machine learning. Tujuan utamanya adalah untuk meminimalkan nilai NRF, di mana nilai yang lebih rendah pada Gambar menunjukkan hasil yang lebih baik. Tabel di bawah memberikan gambaran rinci tentang analisis statistik yang dilakukan pada sampel NRF.

---
![](https://lh3.googleusercontent.com/BsFKs38oFPU48IxzmQbr4P3zUmAoWwEKy3jNvOOq47WZbrnrMc4Uk22SEutjHJ24tM_WN4Tjx9XikUXTN2-T7WXH87vwsEkN5byBAbpHaVKXXpnK20R970CLeFP8FfZ5uCpgiAAoBEssyeqn431KVm8)


---

![](https://lh5.googleusercontent.com/NMhz3FG6wWrfMGPQhwtiUHsQs1-bawVKTHnRyr0BzS24xpX2s-FYzMZ3M3yKmpMezanOg25hpYBfOuWP7KEQzG5fTuMGiHWy-wF6d3fNB9SWNQcbNuEGqWiqw0ipPXVnawG-hmCQ8DcmEdyBLfUVpXU)

---

Dimulai dengan perbandingan antara pendekatan random forest dan autoencoder, terlihat bahwa PhyloMissForest secara konsisten lebih baik dibandingkan dengan metode autoencoder. Ini mencapai nilai NRF rata-rata yang lebih rendah (lebih baik) di sebagian besar persentase data yang hilang. Secara khusus, konfigurasi non-bootstrap memberikan pemulihan pohon filogenetik target yang lebih tepat dibandingkan dengan autoencoder, di seluruh persentase data yang hilang. Dalam skenario bootstrap, tentu terjadi peningkatan performa dibandingkan dengan autoencoder yang terlihat untuk berbagai tingkat data yang hilang.

---

Satu-satunya pengecualian terjadi pada tingkat data yang hilang sebesar 35%, di mana pendekatan autoencoder secara sedikit lebih baik daripada konfigurasi bootstrap. Namun, ketika mempertimbangkan kedua konfigurasi, PhyloMissForest secara konsisten lebih baik daripada autoencoder, mendukung dua kombinasi parameter yang sesuai dengan profil konfigurasi yang dipilih oleh pengguna. Secara statistik, perbaikan ini dianggap signifikan dalam sepuluh dari dua belas kasus, setara dengan tingkat keberhasilan 83,3%, seperti yang dilaporkan dalam Tabel 1.

---

Selanjutnya, jika dibandingkan dengan metode faktorisasi matriks, PhyloMissForest menunjukkan kinerja yang lebih baik. Gambar 2 menggambarkan bahwa pendekatan random forest secara konsisten mencapai nilai NRF rata-rata yang lebih baik di hampir semua tingkat data yang hilang, kecuali dalam skenario dengan 50% entri yang hilang. Dari sudut pandang statistik, perbaikan yang signifikan terlihat dalam setengah dari skenario yang dievaluasi, dengan perbedaan yang paling mencolok terjadi dalam rentang data yang hilang antara 5% hingga 20%.

---

## 2.3.5.2 Kasus 37x37
---
![](https://lh4.googleusercontent.com/YEokKYhNE9nCKRPAOfn3TJbtGNY7CERgDD4Ev8o41aNBSATR80nOsEIgIVTSXZpMncO1HzMJgr4M6kr_EyVckv2B2nG2oHoOI3hfwps3aTajDIkSPpg5Z8RN9eEI9Mf92dzH8vJqsgRjRpPbKV_mC0M)

---
![](https://lh5.googleusercontent.com/X7ACNo4wNwlFIHhoYS8W5RLwGAWWdPWBxd02tyH-GtQpeu4qbv-yWwKXkNbDoxECESySHC_SqoggZcePI9m3S60BE-I-cTLnDjlzmkAkJxEBhb_AdpVNKPVRDDa49JjUffNcLHk0jGYDW2gZl4c5REc)

---

Gambar diatas menampilkan hasil yang diperoleh untuk dataset dengan 37 OTU. Evaluasi melibatkan variasi persentase data yang hilang mulai dari 5% hingga 60%, dengan peningkatan sebesar 5%. Tabel di bawah menyajikan hasil dari pengujian statistik yang dilakukan untuk dataset ini.

---

Ketika kedua konfigurasi parameter dipertimbangkan bersama-sama, kerangka kerja PhyloMissForest secara konsisten mencapai nilai NRF rata-rata yang lebih rendah (lebih baik) dibandingkan dengan metode autoencoder di seluruh tingkat data yang hilang. Saat memeriksa kedua profil konfigurasi secara terpisah, terlihat bahwa PhyloMissForest dengan bootstrap melampaui kinerja autoencoder dalam hal hasil NRF rata-rata untuk semua persentase data yang hilang yang diuji. Perbedaan yang signifikan secara statistik teramati dalam rentang data yang hilang dari 20% hingga 60%. Di sisi lain, konfigurasi non-bootstrap secara statistik mengungguli autoencoder dalam 66,7% dari skenario yang dianalisis. Meskipun autoencoder secara sedikit lebih unggul daripada profil non-bootstrap sebesar 0,5% dalam matriks dengan 10% data yang hilang, perbedaan ini tidak signifikan secara statistik (p-value = 0,97).

---

Dibandingkan dengan metode faktorisasi matriks, PhyloMissForest mencapai nilai NRF rata-rata yang lebih baik dalam enam dari dua belas skenario yang diuji. Namun, pengujian statistik pada sampel NRF mengungkapkan bahwa kedua metode menunjukkan kinerja yang sebanding, menunjukkan perbedaan yang terjadi tidak signifikan dalam dataset ini. Penting untuk dicatat bahwa dataset 37×37 ini berisi data asam amino, yang membuat masalah imputasi data menjadi lebih menantang dibandingkan dengan dataset DNA karena jumlah karakter yang mungkin berbeda. 

---

Dalam skenario yang kompleks seperti ini, waktu eksekusi menggambarkan keunggulan penggunaan PhyloMissForest dibandingkan dengan faktorisasi matriks. Faktorisasi matriks membutuhkan 17 menit dalam dataset ini, sementara PhyloMissForest berhasil menyelesaikan proses imputasi hanya dalam 25 detik dalam profil non-bootstrap atau 7 menit ketika bootstrapping diaktifkan. Ini menunjukkan peningkatan kecepatan yang efektif saat menerapkan kerangka kerja yang diusulkan dalam konteks ini. Analisis yang lebih rinci tentang waktu eksekusi dibahas dalam bagian Hasil.

Ketika membandingkan profil konfigurasi non-bootstrap dan bootstrap yang didukung oleh PhyloMissForest, terlihat bahwa pendekatan bootstrap mengungguli konfigurasi non-bootstrap dalam sepuluh dari dua belas skenario. Oleh karena itu, dengan mengaktifkan bootstrapping, akurasi PhyloMissForest meningkat dalam 83,3% kasus dibandingkan dengan profil konfigurasi yang tidak melibatkan teknik bootstrapping.

---
# 2.3.5.3 Kasus 55x55

---
![](https://lh6.googleusercontent.com/n5rP0WlnNzLtGeUVOH_4NJqQm6F_08N8sWLojV4Lvx_0O1ESQwNcMO3Deu-Q_RYjNPKw5NMihc_zbakRHbWFwofQ2uEv8Jyvopg3_wI6ZH3Pa4FawYkGaqgqnsYKzKkoDVG4PexH4lb1PrDL58XG8Zc)
e
---

![](https://lh5.googleusercontent.com/Vk8BwzNfhjq91vhzMEOh9OSO-eKDNCxZI5na2q2RlIH_jWXVTIrkSu4h9cq_woofj7AZPwIlioxeetfv5L6cpbryxA3WSuInrPlWetd6qFVOlWbA68u-0IJebgDmvHy9JLNVanxAx51_3lACYRt6V1Y)

---



Sama seperti dataset 9×9 dan 37×37, Gambar di atas menampilkan hasil yang dicapai oleh PhyloMissForest bersama metode state-of-the-art dalam sebuah dataset yang terdiri dari 55 OTU. Evaluasi statistik pada sampel NRF (Normalized Robinson-Foulds) diuraikan dalam Tabel di bawah.

---



Ketika membandingkan pendekatan random forest dengan autoencoder, hasil random forest secara konsisten menunjukkan bahwa PhyloMissForest memberikan solusi yang lebih baik dalam semua dua belas persentase data yang hilang yang diuji. Perbaikan dalam skor NRF rata-rata selalu melebihi 6,8% jika dibandingkan dengan metode machine learning lainnya. Hal ini merupakan perbedaan kinerja yang signifikan antara pendekatan random forest dan autoencoder. Pengamatan ini diperkuat oleh hasil analisis statistik, yang mengkonfirmasi pencapaian peningkatan yang signifikan secara statistik dalam semua kasus yang dianalisis.

---

Dalam perbandingan antara pendekatan random forest dan metode faktorisasi matriks, terlihat bahwa PhyloMissForest juga melampaui metode yang bersaing dalam hal kinerja NRF secara keseluruhan. Menurut Tabel 3, peningkatan yang signifikan secara statistik teramati dalam 83% dari skenario yang diuji. Temuan ini menegaskan adanya relevansi kerangka kerja dalam dataset 55x55, terutama ketika menghadapi persentase data yang hilang yang besar. Dalam skenario-skenario sulit ini,  PhyloMissForest mampu melampaui metode faktorisasi matriks, menghasilkan hasil yang 
Mengenai perbandingan antara kasus bootstrap dan non-bootstrap, hasil yang lebih baik teramati ketika strategi bootstrapping digunankan.

---

Dengan memeriksa nilai NRF minimum, dapat disimpulkan bahwa hanya PhyloMissForest yang mampu mencapai 0% NRF dalam setidaknya satu matriks. Selain itu, nilai NRF maksimum yang diperoleh untuk setiap persentase data yang hilang selalu lebih rendah secara konsisten untuk pendekatan random forest dibandingkan dengan teknik state-of-the-art lainnya.

---

![](https://lh6.googleusercontent.com/7cvEv_MvfraAcLBqxlJrUDWTdNZ4iLQ56CL7wL7bA02iWl480W3HFhOAAs3sPiCIr5aQLuX2UDs781gOpWjuy9m93F9-YmBPnQ46s-S8kCNPeRX9nnxk48Y25uJF_HalI5EZJi4F4y_FqzjwEVVTWyw)

---
# Kesimpulan

---

Kami  menggunakan tools yang telah disediakan oleh NCBI yaitu NCBI Virus. Studi kasus ini akan berfokus pada analisis hasil pohon filogenetik yang dikonstruksi dari beberapa data sequence nukleotida virus yang terdapat di database NCBI Virus. Kami akan menganalisis filogenetik SARS-CoV-2 berdasarkan sekuensnya. SARS-CoV-2 adalah virus yang menyebabkan penyakit pernapasan seperti COVID-19 (CoronaVirus Disease 2019). 

---

Oleh karena itu, kami membangun pohon filogenetik berdasarkan kemiripan sekuens untuk mengetahui hubungan kekerabatan antara SARS‑CoV‑2 dengan beberapa virus lainnya yang menyerang sistem pernapasan manusia seperti Human metapneumovirus, Human bocavirus 3, Human rhinovirus 1A, Human Rhinovirus C, Influenza A, Influenza B, Influenza C, dan Influenza D. Kemudian, kami juga membandingkan SARS-CoV-2 dengan virus yang menyerang selain sistem pernapasan seperti Human T-lymphotropic virus 2.
Hasil dari analisis filogenetik dari 9 sekuens virus penyebab infeksi pernapasan dan 1 out group dapat disimpulkan bahwa kladogram terbagi dalam 3 klad. Klad I terdiri dari Human metapneumovirus. Klad II  terdiri dari Human bocavirus 3. Kemudian klad III terdiri dari Rhinovirus C, Influenza A, Influenza D, Rhinovirus A1, Influenza C, Influenza B, dan SARS-CoV-2. 

---

pada Subbab 2.3.5 dilakukan Literature Review pada artikel yang berjudul PhyloMissForest: a random forest framework to construct phylogenetic trees with missing data. Pada artikel tersebut telah ditunjukkan bahwa pengimplementasian imputasi pada matriks jarak yang belum sempurna dengan random forest mengalahkan metode imputasi state-of-the-art lainnya, seperti faktorisasi matriks, dan autoencoder.

---


# Saran
---

Agar penulis atau mahasiswa dapat memahami materi mengenai pembuatan pohon filogenetik, aplikasi rekonstruksi pohon filogenetik, serta analisis hasil pohon filogenetik dan metodologi terbaru terkait rekonstruksi pohon filogenetik (PhyloMissForest) dengan baik, mahasiswa dapat mempelajari mulai dari pemahaman dasar mengenai rekonstruksi pohon filogenetik, penggunaan tools untuk membangun pohon filogenetik seperti NCBI Virus, BioPython dll, dan metodologi terbaru yang mengintegrasikan kecerdasan buatan serta machine learning untuk membangun pohon filogenetik seperti PhyloMissForest. Selain itu, mahasiswa juga harus dapat mengulik lebih dalam materi terkait bioteknologi dan artificial intelligence terlebih lagi dalam konteks bio informasi.





