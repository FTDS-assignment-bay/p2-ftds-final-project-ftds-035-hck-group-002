## 📌 DOOHO – Emotion Detection with YOLOv26n

DOOHO dikembangkan sebagai solusi berbasis *computer vision* untuk mendeteksi dan mengklasifikasikan **emosi wajah manusia** secara otomatis dari citra. Proyek ini dirancang sebagai *early analysis & detection tool* yang dapat membantu sistem digital dalam memahami kondisi emosional pengguna melalui ekspresi wajah. Dengan memanfaatkan pendekatan **object detection** menggunakan model **YOLOv26n**, DOOHO mampu mengenali wajah sekaligus mengklasifikasikan emosi secara efisien dalam satu proses.

Proyek ini sangat relevan untuk digunakan pada berbagai skenario kehidupan sehari-hari dan industri, seperti pembelajaran daring, analisis respons audiens, *human–computer interaction*, serta sistem monitoring visual. Fokus utama DOOHO adalah memastikan kualitas data dan keandalan model melalui proses **Exploratory Data Analysis (EDA)** sebelum tahap pelatihan model dilakukan.

---

## 🧠 Problem Background
Pemahaman emosi manusia melalui ekspresi wajah merupakan tantangan yang kompleks karena tingginya variasi ekspresi, kondisi pencahayaan, sudut pengambilan gambar, serta perbedaan karakteristik individu. Dalam skala data yang besar, proses identifikasi emosi secara manual menjadi tidak efisien dan rentan terhadap subjektivitas.

Selain itu, ketidakseimbangan distribusi kelas emosi (*class imbalance*) dan kualitas anotasi bounding box dapat berdampak langsung pada performa model *deep learning*. Tanpa analisis awal terhadap dataset, model berisiko menghasilkan prediksi yang bias dan kurang akurat. Oleh karena itu, dibutuhkan pendekatan data-driven yang menekankan pemahaman dataset secara menyeluruh sebelum pengembangan model deteksi emosi dilakukan.

---

## 🎯 Project Objective
Berdasarkan permasalahan dalam pengenalan emosi wajah, tujuan dari proyek DOOHO adalah:

1. **Analisis Awal Dataset Emosi**  
   Melakukan Exploratory Data Analysis (EDA) untuk memahami struktur dataset, distribusi kelas emosi, dan kualitas anotasi bounding box.

2. **Minimisasi Bias Model**  
   Mengidentifikasi potensi *class imbalance* dan karakteristik data yang dapat memengaruhi performa model.

3. **Pengembangan Model Deteksi Emosi**  
   Mengembangkan model YOLOv26n yang mampu mendeteksi wajah dan mengklasifikasikan emosi secara simultan.

4. **Dukungan Sistem Interaktif**  
   Menyediakan sistem deteksi emosi yang dapat digunakan sebagai komponen pendukung pada aplikasi interaktif dan sistem analitik.

---

## 📊 Dataset Information
Dataset yang digunakan dalam proyek ini merupakan dataset **Emotion Detection** berformat YOLO yang diperoleh dari **Roboflow Universe**. Dataset ini terdiri dari beberapa kelas emosi wajah yang telah dianotasi menggunakan bounding box dan dibagi ke dalam data training, validation, dan testing.

Dataset ini digunakan sebagai dasar untuk proses Exploratory Data Analysis, training model, evaluasi performa, dan inference.

---

## 🧰 Technology Stack & Libraries
Proyek ini dibangun menggunakan **Python** sebagai bahasa pemrograman utama dengan dukungan library berikut:

| No | Library | Fungsi |
|----|--------|--------|
| 1 | OS | Manajemen direktori dan file dataset |
| 2 | YAML | Membaca konfigurasi dataset YOLO |
| 3 | OpenCV (cv2) | Pengolahan citra dan visualisasi bounding box |
| 4 | NumPy | Operasi numerik dan manipulasi array |
| 5 | Pandas | Pengolahan data tabular hasil EDA |
| 6 | Matplotlib | Visualisasi grafik dan citra |
| 7 | Seaborn | Visualisasi distribusi data |
| 8 | Ultralytics YOLO | Framework object detection YOLOv26n |
| 9 | Torch | Backend deep learning untuk training model |
|10 | Jupyter Notebook | Eksperimen dan dokumentasi proses analisis |

**Tools Pendukung:**
- VSCode / Jupyter Notebook sebagai environment pengembangan
- Roboflow sebagai sumber dan manajemen dataset

---

## 🔄 Data Pipeline & Methodology

### 1. Data Acquisition
Menggunakan dataset emotion detection berformat YOLO dari Roboflow Universe.

### 2. Data Preparation & Validation
- Validasi struktur folder dataset YOLO
- Pemeriksaan konsistensi label dan class ID
- Pembagian data ke dalam train, validation, dan test set

### 3. Exploratory Data Analysis (EDA)
- Analisis distribusi kelas emosi
- Analisis ukuran dan area bounding box
- Visualisasi anotasi bounding box pada citra
- Identifikasi potensi *class imbalance*

### 4. Modeling
- Training model YOLOv26n untuk deteksi emosi wajah
- Monitoring performa training menggunakan learning curve

### 5. Evaluation & Inference
- Evaluasi hasil prediksi pada data test
- Visualisasi hasil inference dengan bounding box dan label emosi

---

## 📦 Project Output
**DOOHO – Emotion Detection System**  
Sistem deteksi emosi wajah berbasis YOLOv26n yang mampu mendeteksi dan mengklasifikasikan ekspresi emosi secara otomatis dari citra.

---

## 📂 Project Structure
```
p2-ftds-final-project-ftds-035-hck-group-002/
│
├── emotion-8/test/images/         # Dataset image untuk testing dan inference
├── runs-2/content/runs/detect/    # Output hasil inference YOLO
│
├── DOOHO_EDA.ipynb                # Exploratory Data Analysis dataset
├── DOOHO_model_training.ipynb     # Training model YOLOv26n
├── DOOHO_learning_curves.ipynb    # Analisis learning curve
├── DOOHO_model_evaluation.ipynb   # Evaluasi performa model
├── DOOHO_inference.ipynb          # Inference model
│
├── DOOHO_logo.png                 # Logo proyek
├── README.md                      # Dokumentasi proyek
└── url.txt                        # Referensi dataset
```

---

## 👥 Project Team – Group 02
- Rifqi Asyrafi  
- Nur Cahyo Widodo  
- Mochamad Rexy Nurulsaputra  
- Sri Probo Aditiyo
