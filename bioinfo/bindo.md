---

marp: true
---

# Microarrays

---
# Pendahuluan

Microarray merupakan teknologi yang serbaguna yang telah merevolusi bidang penelitian biomedis selama dua dekade terakhir. Microarray adalah secara kasat mata adalah benda padat, seperti slide kaca atau chip silikon, di mana berbagai molekul terpasang dalam pola teratur titik-titik mikroskopis. Array ini dapat digunakan untuk menganalisis berbagai interaksi genetik atau biokimia secara bersamaan, menjadikannya alat yang penting dalam memahami biologi yang kompleks pada organisme hidup. Tinjauan literatur ini bertujuan untuk menjelajahi prinsip, aplikasi dari microarray DNA dalam penelitian biomedis.

---

Microarray DNA, sebagai aplikasi spesifik dari teknologi microarray, melibatkan helai kecil DNA tunggal yang disebut "proba." Proba-proba ini umumnya terdiri dari barisan yang spesifik untuk gen yang secara kolektif mencakup seluruh genom yang dikenal. Prinsip dasar dari microarray terletak pada hibridisasi spesifik antara proba-proba ini dan target DNA (cDNA) atau RNA (cRNA) yang komplementer. Ketika target yang diberi label fluoresen ini diterapkan pada microarray, tingkat hibridisasi dalam titik tertentu diukur melalui sinyal fluoresen. Sinyal ini memberikan pengetahuan tentang kelimpahan relatif barisan asam nukleat tertentu dalam sampel, memungkinkan peneliti untuk mengkaji ekspresi genom secara menyeluruh.

---

Dampak microarray DNA pada penelitian biomedis telah sangat besar. Microarray telah memperluas cakupan analisis genetik dari studi satu gen atau sekelompok gen menjadi pemeriksaan menyeluruh terhadap semua gen yang dikenal dalam genom. Dengan memungkinkan analisis yang cepat dan bersamaan, microarray telah memungkinkan peneliti untuk memanfaatkan informasi dari jumlah besar data sekuens yang dihasilkan oleh sekuensing genom secara lengkap. Teknologi ini telah menjadi kunci dalam mempelajari sejumlah fenomena genom yang luas, termasuk:


---

1. Profil Ekspresi Gen: Microarray telah memainkan peran sentral dalam memahami bagaimana gen diekspresikan dalam kondisi normal dan penyakit, memberikan wawasan tentang proses biologis utama.

2. Polimorfisme Satu Nukleotida (SNP): Microarray telah menjadi penting dalam mengidentifikasi variasi genetik yang memengaruhi kerentanan terhadap penyakit dan respons terhadap obat.

3. Variasi Jumlah Salinan DNA: Peneliti telah menggunakan microarray untuk menyelidiki ketidakseimbangan genomik yang terkait dengan berbagai penyakit, termasuk kanker.

---

4. Metilasi DNA: Modifikasi epigenetik, khususnya metilasi DNA, telah dijelajahi menggunakan microarray untuk mengungkap peran mereka dalam regulasi gen.

5. Pemotongan Alternatif: Teknologi ini telah menjadi penting dalam mengungkap regulasi yang kompleks terhadap ekspresi gen melalui pemotongan alternatif.

6. Situs Pengikatan Faktor Transkripsi: Microarray telah memfasilitasi studi interaksi faktor transkripsi, memberikan wawasan tentang jaringan regulasi gen.

---

# Teori Microarray

teknologi microarray, alat fundamental dalam genomika dan analisis ekspresi gen, didasari pada prinsip hibridisasi asam nukleat. Bagian berikut memberikan gambaran tentang teori microarray, menguraikan prinsip-prinsip dan proses inti yang terlibat.

---

1. **Prinsip Teknologi Microarray**:
Microarrays merupakan teknologi yang telah berevolusi dari metode sebelumnya seperti Southern blotting dan hibridisasi blot koloni bakteri, memanfaatkan spesifisitas tinggi dari hibridisasi asam nukleat komplementer. Dalam microarray, proba oligonukleotida pendek terpasang pada solid support, dan sampel asam nukleat yang diberi label diterapkan dalam larutan. Sekuen komplementer antara proba dan sampel asam nukleat mengalami hibridisasi, sedangkan sekuens non-komplementer tidak. Sinyal yang dipancarkan dari label yang terikat kemudian diukur untuk mendeteksi target yang dihibridisasi.

---

2. **Variasi dalam Platform Microarray**:
Banyak platform microarray komersial menggunakan teknologi yang berbeda, tetapi prinsip-prinsip dasarnya tetap konsisten. Sebuah studi yang membandingkan platform populer seperti Affymetrix dan Illumina menemukan bahwa meskipun teknologi yang berbeda, mereka menghasilkan hasil yang serupa ketika diuji dengan sampel RNA yang identik. Array Affymetrix menggunakan proba DNA pendek, sedangkan array Illumina menggunakan proba DNA yang lebih panjang yang terpasang pada manik-manik silika. Hasil analisis ekspresi gen sangatlah serupa di seluruh platform ini.

---

3. **Label Fluoresen dan Deteksi**:
Microarray menggunakan label pewarna fluoresen untuk memvisualisasikan asam nukleat target yang terikat pada proba. Fluorofor memiliki kemampuan untuk memancarkan kembali cahaya yang diserap pada panjang gelombang tertentu. Deteksi fluoresensi menawarkan sensitivitas yang tinggi dan rentang dinamis yang luas, sehingga cocok untuk mengukur target dengan tingkat kelimpahan yang bervariasi. Dalam microarray profil ekspresi dua warna, sampel yang berbeda yang diberi label dengan pewarna yang berbeda dapat dibedakan berdasarkan warna cahaya yang dipancarkan. Diferensiasi berbasis warna ini menjadi dasar untuk menganalisis tingkat ekspresi gen relatif.

---

4. **Penghasilan Data dan Tantangan**:
Eksperimen microarray menghasilkan jumlah data yang besar, dengan satu eksperimen biasanya menggunakan beberapa microarray individu. Sekarang sebuah array dapat berisi jutaan proba. Memproses dan menginterpretasi data ini membutuhkan metode yang tepat. Pra-pemrosesan intensitas sinyal fluoresensi mentah melibatkan pengurangan noise latar belakang dan normalisasi untuk memperbaiki variasi dari sinyal nonbiologis. Metode normalisasi umum termasuk normalisasi lowess dan normalisasi kuantil. Setelah data diproses, tujuan utamanya adalah mengidentifikasi sinyal yang signifikan secara statistik, yang kemudian dapat digunakan untuk analisis selanjutnya yang disesuaikan berdasarkan pertanyaan penelitian tertentu.

---

# Microarray Analysis

Langkah pertama dalam melakukan analisis microarray adalah perencanaan desain eksperimen, fase yang sangat penting yang merupakan dasar keberhasilan dan interpretasi dari eksperimen. Pertimbangan dan pengambilan keputusan yang hati-hati sangat penting selama fase ini untuk memastikan tujuan eksperimen microarray tercapai. Berikut adalah aspek kunci yang harus dipertimbangkan selama fase ini:

--- 

1. **Definisikan Tujuan Penelitian**: Pada tahap ini, para peneliti harus dengan jelas mendefinisikan tujuan dari eksperimen microarray. Ini melibatkan menentukan pertanyaan penelitian, tujuan, dan wawasan biologis yang akan diperoleh dari analisis. Fase ini adalah kesempatan untuk memperkirakan dan merencanakan tantangan teknis potensial yang mungkin muncul selama eksperimen.

2. **Konsultasi dengan Ahli statistik**: Eksperimen microarray sering membutuhkan pemahaman yang kuat tentang statistik untuk mencapai hasil yang baik. Para peneliti didorong untuk berkonsultasi dengan seorang statistisi, terutama jika keahlian mereka dalam analisis statistik terbatas, untuk memastikan bahwa desain eksperimen secara statistik dapat dipertanggungjawabkan.

3. **Memilih Microarray vs. Sequencing**: Para peneliti harus memutuskan apakah akan menggunakan microarray atau metode sekuensing generasi berikutnya berdasarkan tujuan penelitian. Pilihan ini harus sesuai dengan informasi spesifik yang dibutuhkan dan sumber daya yang tersedia.

---

4. **Mengoptimalkan Variabel**: Untuk meningkatkan kemungkinan memperoleh data dengan signifikansi statistik, disarankan untuk membatasi jumlah variabel yang diuji, terutama pada tahap awal eksperimen. Fokus pada satu variabel (misalnya, dosis dan durasi obat) menyederhanakan analisis dan mengurangi jumlah microarray dan sampel yang diperlukan. Studi optimasi dosis awal dapat bermanfaat.

5. **Menentukan Replikasi Biologis**: Jumlah replikasi biologis yang diperlukan harus ditentukan dengan hati-hati. Replikasi biologis adalah sampel yang diperoleh dari sumber independen yang berbeda (misalnya, tumor, hewan, atau kultur sel yang terpisah). Replikasi biologis yang memadai sangat penting untuk menilai secara andal perbedaan yang signifikan secara statistik di atas tingkat variasi alami dalam populasi.

---

6. **Eksperimen Pilot**: Melakukan eksperimen pilot dapat sangat berharga untuk memperkirakan variabilitas ekspresi gen antar sampel. Eksperimen pilot ini dapat melibatkan transkripsi balik reaksi berantai polimerase kuantitatif (qRT-PCR) untuk gen yang dipilih atau analisis microarray skala kecil untuk mengevaluasi varians ekspresi gen dan mengatasi tantangan teknis yang tidak terduga.

7. **Pemilihan Sampel**: Sampel yang akan dibandingkan harus mewakili kondisi yang diuji secara akurat. Para peneliti harus merencanakan dan, jika perlu, mempraktikkan metode untuk mendapatkan sampel yang mencerminkan kondisi masing-masing. Hal ini dapat melibatkan isolasi atau pengayaan populasi sel tertentu untuk memastikan analisis ekspresi gen yang akurat.

---

8. **Memilih Platform Microarray yang Sesuai**: Pilihan platform microarray harus sesuai dengan tujuan eksperimen. Pertimbangan harus diberikan kepada sumber daya yang tersedia di lembaga penelitian. Jika informasi spesifik, seperti ekspresi isoform pemotongan, diperlukan, pilih platform microarray dengan proba yang mencakup fitur gen yang relevan dan situs sambungan pemotongan yang diketahui.

---


## Microarray sample preparation

Langkah kedua dalam analisis microarray adalah fase persiapan sampel yang penting, yang melibatkan memperoleh materi genetik yang diperlukan untuk analisis, biasanya RNA atau DNA. Langkah ini sangat penting karena secara signifikan memengaruhi keberhasilan atau kegagalan seluruh eksperimen microarray.

---

1. **Sumber Sampel**: Proses dimulai dengan pengumpulan sel atau jaringan yang mengandung materi genetik yang diminati. Pilihan sumber sampel tergantung pada tujuan penelitian tertentu dan dapat bervariasi secara luas.

2. **Ekstraksi RNA atau DNA**: Untuk analisis RNA dan DNA, sangat penting untuk mengekstraksi materi genetik berkualitas tinggi. Sementara ekstraksi DNA umumnya dapat diandalkan, ekstraksi RNA membutuhkan perawatan khusus karena ketidakstabilannya yang melekat dan kerentanannya terhadap degradasi. Kualitas RNA yang diekstraksi memiliki dampak besar pada akurasi dan keandalan data ekspresi gen selanjutnya.

3. **Penanganan RNA**: Penanganan RNA sangat penting untuk mencegah degradasi. Jika RNA mengalami degradasi secara signifikan selama penanganan atau penyimpanan, data ekspresi gen yang dihasilkan akan berkualitas buruk. Tindakan pencegahan khusus harus diambil untuk mempertahankan integritas RNA.

---

4. **Pengayaan dan Amplifikasi (jika diperlukan)**: Bergantung pada desain eksperimen dan jumlah RNA yang tersedia, berbagai protokol dapat diterapkan. RNA total dapat digunakan secara langsung, atau dapat diperkaya untuk mRNA melalui pemurnian afinitas atau deplesi RNA ribosom. Dalam kasus di mana jumlah RNA terbatas, langkah amplifikasi dapat dilakukan untuk meningkatkan jumlah materi genetik.


5. **Labeling**: Tahap akhir dari persiapan sampel melibatkan pelabelan asam nukleat yang akan diterapkan pada mikroarray. Materi genetik dapat dilabeli langsung dengan pewarna, atau dapat diubah menjadi cDNA (DNA komplementer) melalui transkripsi balik. Pewarna dapat dimasukkan selama sintesis cDNA atau dalam tahap transkripsi berikutnya untuk membuat cRNA (RNA komplementer). Asam nukleat yang dilabeli mewakili kelimpahan relatif transkrip endogen yang diekspresikan dalam sampel biologis asli.

---


# Hybridization, Washes, and Scanning
Langkah ketiga dalam analisis microarray melibatkan proses penting hibridisasi, pencucian, dan pemindaian, yang sangat penting untuk memperoleh data dari eksperimen microarray.

---

1. **Hibridisasi**: Dalam langkah ini, sampel yang diberi label diterapkan dalam larutan ke microarray. Sampel yang diberi label mengandung materi genetik atau biomolekul yang diminati, dan diperbolehkan untuk mengalami hibridisasi dengan sekuens proba komplementer yang terimobilisasi pada microarray. Proses hibridisasi ini memungkinkan materi genetik sampel untuk berikatan dengan titik-titik tertentu pada microarray di mana sekuens komplementer hadir.

2. **Pencucian**: Setelah hibridisasi, serangkaian langkah pencucian dilakukan untuk menghilangkan molekul sampel yang tidak terikat atau terikat secara non-spesifik. Langkah ini sangat penting untuk memastikan spesifisitas dan akurasi hasil. Semua materi yang tidak terikat dicuci, meninggalkan hanya materi genetik yang secara khusus mengalami hibridisasi dengan proba pada microarray.

3. **Label Fluoresen (jika berlaku)**: Dalam kasus di mana sampel diberi label dengan biotin, seperti dengan platform Affymetrix, streptavidin yang diberi label fluoresen diterapkan. Streptavidin adalah protein yang berikatan secara spesifik dengan biotin. Langkah ini membantu dalam pelabelan dan visualisasi lebih lanjut molekul yang dihibridisasi pada microarray.

---

4. **Pemindaian**: Setelah mikroarray disiapkan, laser digunakan untuk merangsang fluorophore yang terikat pada setiap titik pada array. Fluorophore yang terikat ini memancarkan sinyal fluoresen pada panjang gelombang tertentu, dan intensitas sinyal yang dipancarkan diukur dan direkam. Proses ini menghasilkan gambar mikroarray, biasanya dalam format Tagged Image File Format (TIFF). Dalam gambar ini, setiap gen atau target sesuai dengan titik tertentu pada mikroarray, dan intensitas sinyal fluoresen mencerminkan ekspresi relatif dari gen atau target tersebut. Gambar ini memberikan representasi visual dari hibridisasi dan memungkinkan untuk kuantifikasi tingkat ekspresi gen.

---

# Data analyses

proses analisis data dalam analisis microarray melibatkan beberapa langkah penting. Awalnya, gambar microarray mentah diproses menggunakan perangkat lunak khusus yang disediakan oleh platform microarray utama. Perangkat lunak ini secara akurat mengidentifikasi intensitas hibridisasi proba, lokasi spot, dan membedakannya dari artefak potensial seperti debu atau goresan. Intensitas setiap piksel dalam spot diukur, dan berbagai statistik (rata-rata, median, atau intensitas piksel terintegrasi) dihitung untuk setiap spot. Nilai intensitas hibridisasi akhir untuk setiap spot dihitung dengan mengurangi intensitas hibridisasi latar belakang rata-rata di daerah sekitarnya.

---

nilai intensitas ini kemudian diterjemahkan menjadi pengganti untuk tingkat ekspresi gen atau target relatif, menghasilkan lembaran kerja nilai ekspresi untuk analisis statistik lebih lanjut. Nilai ekspresi ini sering digambarkan sebagai rasio antara sampel uji dan referensi, dengan transformasi umum menjadi logaritma basis 2 (rasio log2) untuk memberikan spektrum nilai yang kontinu yang menunjukkan target yang diatur naik atau turun.

---


metode khusus untuk pra-pemrosesan data, kontrol kualitas, normalisasi, dan analisis selanjutnya dapat bervariasi tergantung pada platform microarray, jenis sampel, dan tujuan penelitian. Berbagai paket perangkat lunak analisis data komersial dan open-source tersedia, dengan Bioconductor menjadi platform open-source yang banyak digunakan. Konsultasi dengan seorang biostatistik yang akrab dengan analisis data microarray disarankan untuk pengguna pemula. Selain itu, mematuhi pedoman Minimum Information About a Microarray Experiment (MIAME) penting untuk memastikan reproduktibilitas dan interpretasi hasil.

---

Hasil utama dari analisis data microarray biasanya adalah daftar gen target yang menunjukkan perbedaan ekspresi yang signifikan antara kondisi yang diminati. Pemilihan ambang batas untuk mendefinisikan sinyal yang terdeteksi dan penentuan tingkat ekspresi diferensial yang signifikan melibatkan metode statistik, seperti menghitung tingkat penemuan palsu. Data yang dihasilkan sering disajikan dalam peta panas grafis, secara visual mewakili di bawah atau di atas ekspresi gen target.

---

Dalam eksperimen microarray, karena potensi kelimpahan target yang signifikan, umumnya dilakukan pengelompokan gen berdasarkan ontologi gen, yang mencakup fungsi molekuler, lokalisasi seluler, jalur yang diketahui, dan proses biologis. Analisis pengkayaan set gen ini membantu mengidentifikasi set gen yang secara kolektif berkontribusi pada fenotipe tertentu, bahkan jika perubahan gen individu kecil. Dalam analisis klaster, gen dikelompokkan berdasarkan perubahan tingkat ekspresi yang serupa, memungkinkan eksplorasi gen yang mungkin terlibat dalam proses biologis atau fenotipe yang sama.


---

# Aplikasi

Teknologi microarray menawarkan berbagai aplikasi selain perbandingan profil ekspresi gen. Tinjauan literatur ini merangkum berbagai aplikasi dari microarray:

**1. Supervised vs. Unsupervised Analyses**:
    - Dalam analisis supervised, para peneliti menggunakan pengetahuan sebelumnya untuk mengidentifikasi dan mempelajari gen atau jalur tertentu yang menarik berdasarkan perbedaan ekspresi yang signifikan antara kondisi.
    - Analisis unsupervised lebih eksploratif dan tidak dibatasi oleh harapan sebelumnya. Seringkali melibatkan teknik pembelajaran mesin, seperti pengelompokan, untuk mengelompokkan gen atau sampel dengan pola ekspresi yang serupa. Analisis unsupervided dapat mengarah pada penemuan informasi baru dan identifikasi gen baru yang terkait dengan proses atau hasil klinis tertentu.

---

**2. Penemuan Kelas**:
    - Analisis unsupervised, terutama pengelompokan, berguna untuk penemuan kelas, di mana sampel dengan profil ekspresi gen yang serupa dikelompokkan bersama. Metode ini membantu mengungkap pola dan hubungan dalam data tanpa pengetahuan biologis sebelumnya.
    - Penemuan kelas dapat diterapkan untuk mengidentifikasi subtipe penyakit, seperti berbagai jenis kanker, berdasarkan pola ekspresi gen mereka. Informasi ini dapat digunakan dalam pengaturan klinis untuk mengidentifikasi sumber utama metastasis atau memprediksi prognosis pasien.

---

**3. Prediksi Kelas**:
    - Prediksi kelas adalah aplikasi lain dari pembelajaran mesin dan mikroarray. Ini melibatkan penggunaan profil ekspresi gen dari kelas sampel yang diketahui untuk memprediksi kelas sampel yang tidak diketahui. Misalnya, ini dapat membantu mengklasifikasikan berbagai jenis kanker berdasarkan tanda-tanda ekspresi gen mereka.
    
---

**4. Kebermanfaatan Klinis**:
    - Mikroarray dapat berharga dalam aplikasi klinis ketika perubahan dalam ekspresi beberapa gen memberikan data yang lebih informatif daripada penanda individu atau penanda penyakit saat ini.
    - Penggunaan klinis mikroarray dibenarkan ketika informasi yang diperoleh dari array dapat mempengaruhi keputusan manajemen pasien, meningkatkan hasil pasien, dan terbukti hemat biaya.

---

**5. Analisis Fitur Genomik DNA**:
    - Microarray digunakan untuk menganalisis fitur genomik DNA, termasuk deteksi variasi jumlah salinan (delesi atau duplikasi) melalui hibridisasi genomik komparatif array (array CGH).
    - Mereka digunakan dalam studi asosiasi genomik seluruh genom (GWAS) untuk mengidentifikasi polimorfisme nukleotida tunggal (SNP) yang terkait dengan penyakit tertentu.

---

**6. Interaksi DNA-Protein dan Analisis Metilasi DNA**:
    - Microarray memfasilitasi analisis genomik efisien dari metilasi DNA dan interaksi DNA-protein seluruh genom.
    - Imunopresipitasi (IP) yang dikombinasikan dengan microarray memungkinkan peneliti untuk mengidentifikasi gen yang termetilasi dengan memurnikan fragmen DNA termetilasi menggunakan antibodi anti-metilsitidin.
    - Kompleks DNA-protein dapat diisolasi dan diidentifikasi menggunakan antibodi spesifik untuk protein yang diketahui mengikat DNA dalam eksperimen imunopresipitasi kromatin-on-chip (ChIP-on-chip).
    - Perlu dicatat bahwa sekuensing imunopresipitasi kromatin (ChIP-Seq) telah banyak menggantikan microarray untuk eksperimen ChIP karena spesifisitasnya yang lebih baik.
