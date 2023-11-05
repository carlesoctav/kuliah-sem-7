Judul: Microarray dalam Penelitian Biomedis: Tinjauan Komprehensif

Pendahuluan

Microarray merupakan teknologi yang serbaguna yang telah merevolusi bidang penelitian biomedis selama dua dekade terakhir. Microarray adalah secara kasat mata adalah benda padat, seperti slide kaca atau chip silikon, di mana berbagai molekul terpasang dalam pola teratur titik-titik mikroskopis. Array ini dapat digunakan untuk menganalisis berbagai interaksi genetik atau biokimia secara bersamaan, menjadikannya alat yang penting dalam memahami biologi yang kompleks pada organisme hidup. Tinjauan literatur ini bertujuan untuk menjelajahi prinsip, aplikasi dari microarray DNA dalam penelitian biomedis.

Microarray DNA, sebagai aplikasi spesifik dari teknologi microarray, melibatkan helai kecil DNA tunggal yang disebut "proba." Proba-proba ini umumnya terdiri dari barisan yang spesifik untuk gen yang secara kolektif mencakup seluruh genom yang dikenal. Prinsip dasar dari microarray terletak pada hibridisasi spesifik antara proba-proba ini dan target DNA (cDNA) atau RNA (cRNA) yang komplementer. Ketika target yang diberi label fluoresen ini diterapkan pada microarray, tingkat hibridisasi dalam titik tertentu diukur melalui sinyal fluoresen. Sinyal ini memberikan pengetahuan tentang kelimpahan relatif barisan asam nukleat tertentu dalam sampel, memungkinkan peneliti untuk mengkaji ekspresi genom secara menyeluruh.

Dampak microarray DNA pada penelitian biomedis telah sangat besar. Microarray telah memperluas cakupan analisis genetik dari studi satu gen atau sekelompok gen menjadi pemeriksaan menyeluruh terhadap semua gen yang dikenal dalam genom. Dengan memungkinkan analisis yang cepat dan bersamaan, microarray telah memungkinkan peneliti untuk memanfaatkan informasi dari jumlah besar data sekuens yang dihasilkan oleh sekuensing genom secara lengkap. Teknologi ini telah menjadi kunci dalam mempelajari sejumlah fenomena genom yang luas, termasuk:

1. Profil Ekspresi Gen: Microarray telah memainkan peran sentral dalam memahami bagaimana gen diekspresikan dalam kondisi normal dan penyakit, memberikan wawasan tentang proses biologis utama.

2. Polimorfisme Satu Nukleotida (SNP): Microarray telah menjadi penting dalam mengidentifikasi variasi genetik yang memengaruhi kerentanan terhadap penyakit dan respons terhadap obat.

3. Variasi Jumlah Salinan DNA: Peneliti telah menggunakan microarray untuk menyelidiki ketidakseimbangan genomik yang terkait dengan berbagai penyakit, termasuk kanker.

4. Metilasi DNA: Modifikasi epigenetik, khususnya metilasi DNA, telah dijelajahi menggunakan microarray untuk mengungkap peran mereka dalam regulasi gen.

5. Pemotongan Alternatif: Teknologi ini telah menjadi penting dalam mengungkap regulasi yang kompleks terhadap ekspresi gen melalui pemotongan alternatif.

6. Situs Pengikatan Faktor Transkripsi: Microarray telah memfasilitasi studi interaksi faktor transkripsi, memberikan wawasan tentang jaringan regulasi gen.

IN PRINCIPLE
Microarrays, much like the earlier methods of Southern blotting and bacterial
colony blot hybridization, exploit the high specificity under stringent condi-
tions with which complementary nucleic acid strands hybridize [1]. In these

earlier blotting methods, DNA samples attached to a membrane are probed
with a labeled oligonucleotide in solution. Microarrays function in the reverse-
oligonucleotide probes are attached to a supporting structure and labeled sam-
ple nucleic acids are applied in solution to the probe-bearing surface. In both
cases, labeled nucleic acids that fail to hybridize with attached sequences are
washed away, in principle solely due to a lack of perfect complementarity.
Targets hybridized to corresponding probes are then detected by measuring
signals emitted from persistently bound labels (Fig. 4.1).
There are variations on this theme between different commercially avail-
able microarrays, but the same principles apply across platforms. An illustra-
tion of this was presented in a large multicenter comparison of microarrays that
included popular platforms made by Affymetrix and Illumina [2]. These plat-
forms apply very different technologies—Affymetrix microarrays employ short
perfect match and mismatch DNA probes directly synthesized onto a glass slide,
while Illumina arrays have long DNA probes attached to silica beads that sit in
tiny wells on a slide. When identical samples of RNA were tested, Affymetrix

nd Illumina arrays consistently gave very similar results with a high degree of
overlap in differentially expressed genes.
The labels used to visualize target nucleic acids bound to microarrays are
fluorophores or dyes, which have the useful ability to re-emit absorbed light at a
specific wavelength, or color. Detection of fluorescence can be highly sensitive
and provide a fairly wide dynamic range, both important qualities when used to
detect targets that can vary in abundance over several logarithmic orders of mag-
nitude. Additionally, two samples labeled with different dyes applied to the same
microarray can be distinguished by the color of light they emit. This is the basis
for 2-color expression profiling microarrays in which the ratio of the colors pro-
duced by bound targets to a certain probe reflects the relative expression between
the two samples. In contrast, with 1-color profiling, each sample is labeled with
the same color dye but applied to separate microarrays, and relative expression
is measured by comparing signal intensity between the two arrays (Fig. 4.1).
A microarray experiment generates large amounts of data, and converting
this data into valid and meaningful information is key to unlocking its scien-
tific potential. A single experiment utilizes multiple individual microarrays, and
as probe density has increased to provide better genomic coverage, a single
array may contain millions of different probes. For instance, the Affymetrix
GeneChip Human Transcriptome Array 2.0 currently contains over six million
distinct probes. Processing and interpreting such vast amounts of raw data can
be challenging, but over the years methods have become well developed. Before
the main data analysis, raw fluorescence signal intensities must be preproc-
essed into signals adjusted for technical sources of variation. This step involves
subtraction of background noise by methods that can vary between platforms,
and then normalization to correct for nonbiological sources of signal variation.
There are different approaches to normalization, but in general when only a
small fraction of targets are expected to change between conditions, there are
two equally popular normalization methods: lowess normalization and quantile
normalization [3]. After the data has been preprocessed, one can proceed to the
primary task of identifying statistically significant signals and apply this infor-
mation in subsequent analyses tailored to address a specific research question.


IN PRACTICE
A typical microarray experiment workflow has the following steps: experimen-
tal design planning, sample preparation, hybridization, and washes, scanning,
data analysis, and result validation (Fig. 4.2). Here we will give a brief overview
of each step in this workflow.
Experimental Design Planning
As with any scientific experiment, careful planning is essential to achieve the
goals of a microarray experiment. This is the time to clearly define the goals and
to anticipate technical challenges that may arise. Since microarray experiments

by their nature require a good knowledge of statistics, now is the time to consult
a statistician if needed. Also, with the availability of next-generation sequencing
approaches, one should decide whether to use microarrays over sequencing (see
below for further discussion).
A major objective of planning is to design the experiment to give the best
chance of obtaining data with statistical significance. That is, to find expres-
sion level differences caused by biological differences, not by chance alone.
One aspect of this is to limit, at least initially, the number of variables being


tested—in other words, keep it simple. It is easier to test the effect of a drug given
at a single dose and single duration than it is to test the effects of several different
doses given over several different durations. The latter would require many more
microarrays and samples in order to obtain significant data for each of the dif-
ferent combinations of dose and duration. For this reason, a preliminary analysis
of the variables being tested, such as a dose optimization study, may be helpful.
Another important aspect in planning is to determine how many biologi-
cal replicates are needed. Biological replicates are samples from multiple inde-
pendent sample sources, such as separate tumors, animals, or cell line cultures.
It is only through repeated microarray analyses with a sufficient number of
biological replicates that statistically significant differences above the level of
natural variation across a population can be reliably assessed. To illustrate this,
let’s compare samples from a highly inbred strain of mice versus samples from
human patients. The natural variation of gene expression in the mice is gener-
ally lower than in the patient samples. Thus, while a microarray experiment
analyzing the mice may only require a handful of samples per condition, the
human study may require samples from a large number of patients to account
for the greater variability. Note that biological replicates are not technical rep-
licates, which are repeated samples from the same source. Technical replicates
are mainly useful for assessing technical variability in the microarray procedure
itself, which is generally a smaller factor than biological variability and have
largely been dealt with by the microarray manufacturer

Unfortunately, the question of how many biological replicates are needed
can sometimes be difficult to answer with certainty. This is because different
types of samples and the methods of obtaining them can yield wide variability
in the resulting gene expression profiles. For example, a uniform cultured cell
line will usually have less variability from plate to plate than tumors from surgi-
cal resection of different patients. To address this problem, it is a good idea to
perform a pilot experiment aimed at assessing the range of gene expression vari-
ability between samples. One may do this by reverse transcription quantitative
polymerase chain reaction (qRT-PCR) for several genes known or suspected
to vary in expression across samples. A better approach, particularly for larger
studies, may be to perform a pilot microarray analysis on a small number of
samples first. This will not only give an estimate of gene expression variance
across the whole range of genes on the array, but may also reveal unforeseen
technical difficulties that need to be addressed before starting the main experi-
ment. Once variance in gene expression is estimated for the system, one can
calculate the number of biological replicates needed to detect the proposed
minimum significant change (effect size) at an appropriate level of significance
and statistical power.
Naturally, to find real biological expression differences between the condi-
tions being tested, the samples to be compared must represent, as closely as pos-
sible, each respective condition. Again, taking the example of cultured cell lineS

versus patient tumors, this can be relatively straightforward when, for example,
assessing the effect of a certain drug on cultured cells. As long as the cells
remain similarly viable under each condition, the difference is primarily limited
to the treatment administered, experimental or control. Tumors, on the other
hand, are composed of heterogeneous populations of cells, which may include
stromal cells, epithelial cells, endocrine-type cells, various types of blood cells,
and more. If one is only interested in the gene expression differences within a
single population of cells in the tumors, then a method to isolate or significantly
enrich for this population is needed. Otherwise the gene expression of admixed
cells may obscure the true expression pattern of the cells of interest. Thus, one
should carefully plan, and ideally practice beforehand, the optimal method for
obtaining the desired samples.
Finally in the planning stage, one should select a suitable microarray plat-
form designed to provide the type of information needed for the goals of the
experiment. The choice of platform may be dictated largely by which resources
are available at your institution, but even then it is important to make sure the
available platform is suitable before proceeding further. For example, if one is
interested in analyzing variations in splice isoform expression, one should use
microarrays with probes covering gene expression across all known individual
exons. It would also be desirable for the array to include probes containing
known splice junction sites, allowing for analysis of splicing events associated
with specific splice isoform expression.



Sample Preparation
Once the desired sample cells or tissues are obtained, one may proceed to RNA
or DNA extraction. Given its stability, extraction of high-quality DNA is gener-
ally reliable in most hands without taking special precautions. RNA, however,
is more labile and prone to degradation. Therefore, among the steps in a typical
microarray experiment, RNA extraction and handling probably has the greatest
impact on success or failure of the experiment. If the sample RNA has degraded
substantially, then expression data derived from such RNA will be correspond-
ingly poor. (See Troubleshooting section below for more on this.)
After RNA isolation, different platforms have differing protocols that lead
to the final labeled nucleic acid sample that is to be applied to the microarray.
Total RNA may be used directly or enriched for mRNA by affinity purification
or depletion of ribosomal RNA. An amplification step can also be performed if
the quantity of RNA is limiting. RNA may then be dye-labeled directly or, more
commonly, converted to cDNA by reverse transcription. Dyes may be incor-
porated during cDNA synthesis or in a subsequent transcription step to make
cRNA. In any case, the final product of sample preparation is a collection of
dye-labeled complementary nucleic acids representing the relative abundance
of endogenous transcripts expressed in the original biologic sample



Hybridization, Washes, and Scanning
Labeled sample is then applied in solution to the microarray for hybridization
with complementary probe sequences. This is followed by a series of wash steps
to remove unbound sample. If the sample was labeled with biotin (as with the
Affymetrix platform) fluorescently labeled streptavidin is then applied. The
microarray is now ready for scanning. A laser excites bound fluorophores at
each spot on the array, and the emitted fluorescent signal intensity at the appro-
priate wavelength is measured and recorded. This yields an image of the micro-
array [typically in Tagged Image File Format (TIFF) format] wherein each gene
or target corresponds to a single spot, and the relative expression of that gene or
target is reflected in a measurable intensity of hybridization (Fig. 4.3)

