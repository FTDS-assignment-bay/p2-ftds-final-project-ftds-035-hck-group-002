<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?font=Open+Sans&weight=1500&size=30&duration=3000&pause=800&color=8A2BE2&center=true&vCenter=true&width=1200&lines=Hello+There!;This+is+DOHOO:+Emotion+Detection+with+YOLOv26n" />
</p>

<p align="center">
  <img src="DOOHO_logo.png" width="200"/>
</p>

<h1 align="center">DOOHO</h1>
<p align="center">
  <span style="font-weight:500; font-size:22px; color:#2E8B57;">
    From Impressions to ROI
  </span>
</p>


# About DOOHO
Di tengah riuhnya kota, iklan Digital Out-of-Home (DOOH) adalah raksasa yang tak terhindarkan. Dari layar megah di gedung pencakar langit hingga monitor interaktif di dalam MRT, potensi jangkauannya masif. Namun, selama bertahun-tahun, marketer menghadapi satu misteri besar: **Bagaimana kita mengukur dampaknya secara nyata?** Tanpa data akurat, DOOH sering kali menjadi investasi yang sulit dilacak keberhasilannya dalam marketing funnel.

DOOHO hadir sebagai jawaban atas kegelisahan tersebut. Kami bukan sekadar sistem pemantauan kami adalah "mata" cerdas bagi brand Anda. Menggunakan teknologi observasi mutakhir, DOOHO mampu memetakan audiens yang terpapar iklan secara real-time. Lebih jauh lagi, kami menganalisis ekspresi dan reaksi emosional mereka dan memberikan data objektif tentang apakah iklan Anda benar-benar menyentuh hati mereka atau sekadar lewat begitu saja. Bersama DOOHO, ubah tebakan menjadi data, dan ubah ekspresi menjadi strategi.

# Problem Background
Pemahaman emosi manusia melalui ekspresi wajah merupakan tantangan yang kompleks karena tingginya variasi ekspresi, kondisi pencahayaan, sudut pengambilan gambar, serta perbedaan karakteristik individu. Dalam skala data yang besar, proses identifikasi emosi secara manual menjadi tidak efisien dan rentan terhadap subjektivitas.

Selain itu, ketidakseimbangan distribusi kelas emosi (*class imbalance*) dan kualitas anotasi bounding box dapat berdampak langsung pada performa model *deep learning*. Tanpa analisis awal terhadap dataset, model berisiko menghasilkan prediksi yang bias dan kurang akurat. Oleh karena itu, dibutuhkan pendekatan data-driven yang menekankan pemahaman dataset secara menyeluruh sebelum pengembangan model deteksi emosi dilakukan.

# Project Objective
Berdasarkan permasalahan dalam pengenalan emosi wajah, tujuan dari proyek DOOHO adalah:

1. **Analisis Awal Dataset Emosi**  
   Melakukan Exploratory Data Analysis (EDA) untuk memahami struktur dataset, distribusi kelas emosi, dan kualitas anotasi bounding box.

2. **Minimisasi Bias Model**  
   Mengidentifikasi potensi *class imbalance* dan karakteristik data yang dapat memengaruhi performa model.

3. **Pengembangan Model Deteksi Emosi**  
   Mengembangkan model YOLOv26n yang mampu mendeteksi wajah dan mengklasifikasikan emosi secara simultan.

4. **Dukungan Sistem Interaktif**  
   Menyediakan sistem deteksi emosi yang dapat digunakan sebagai komponen pendukung pada aplikasi interaktif dan sistem analitik.

# Dataset
Dataset yang digunakan dalam proyek ini merupakan dataset **Emotion Detection** berformat YOLO yang diperoleh dari **Roboflow Universe**. Dataset ini terdiri dari 7 kelas emosi wajah yang telah dianotasi menggunakan bounding box dan dibagi ke dalam data training, validation, dan testing.

Dataset ini digunakan sebagai dasar untuk proses Exploratory Data Analysis, training model, evaluasi performa, dan inference.  
[Dataset](https://universe.roboflow.com/spacex-bmpib/emotion-gyup3/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true) - Sumber Dataset

# Stack
| No | Stack           |
|----|-----------------|
| 1  | Python          |
| 2  | Roboflow        |
| 3  | Ultralytics YOLO|
| 4  | OpenCV          |
| 5  | NumPy           |
| 6  | Matplotlib      |
| 7  | Pandas          |
| 8  | Seaborn         |
| 9  | Pillow          |
| 10 | PyYAML          |
| 11 | Streamlit       |
| 12 | Hugging Face    |
| 13 | Jupyter/Colab   |

# Deployment
[Try DOOHO on Hugging Face](https://huggingface.co/spaces/ncahyow/Yolo_Detection)

# Project Team – Group 02
- Rifqi Asyrafi  
- Nur Cahyo Widodo  
- Mochamad Rexy Nurulsaputra  
- Sri Probo Aditiyo