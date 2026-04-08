# 🛍️ ETL Pipeline - Fashion Studio Competitor Data

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk membangun **ETL (Extract, Transform, Load) Pipeline sederhana** untuk mengambil data produk dari website kompetitor di bidang fashion.

Data yang diambil akan digunakan oleh tim data science untuk analisis harga dan produk kompetitor.

---

## 🌐 Sumber Data

Website:
https://fashion-studio.dicoding.dev/

Data yang diambil:

* Title
* Price
* Rating
* Colors
* Size
* Gender

---

## ⚙️ Arsitektur ETL

### 1. Extract

Mengambil data dari seluruh halaman website (halaman 1–50) menggunakan teknik web scraping.

### 2. Transform

Membersihkan dan memproses data:

* Menghapus data invalid (Unknown Product, Invalid Rating, dll)
* Mengubah harga dari USD ke IDR (kurs Rp16.000)
* Mengubah rating menjadi float
* Mengambil angka dari kolom Colors
* Membersihkan kolom Size dan Gender
* Menghapus data null dan duplikat

### 3. Load

Menyimpan data bersih ke dalam file:

```
products.csv
```

---

## 📁 Struktur Proyek

```
submission-pemda/
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
├── utils/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── main.py
├── requirements.txt
├── products.csv
├── submission.txt
```

---

## 🚀 Cara Menjalankan Proyek

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan ETL Pipeline

```bash
python main.py
```

Output:

* Data hasil transformasi akan tersimpan di `products.csv`

---

## 🧪 Menjalankan Unit Test

```bash
pytest tests/
```

---

## 📊 Menjalankan Test Coverage

```bash
pytest --cov=utils tests/
```

---

## ✅ Kriteria Data Hasil

Data hasil akhir memenuhi:

* Tidak ada nilai null
* Tidak ada data duplikat
* Tidak ada data invalid
* Price dalam rupiah
* Rating dalam bentuk float
* Colors dalam bentuk integer
* Size dan Gender dalam format bersih

---

## 🛠️ Teknologi yang Digunakan

* Python
* requests
* BeautifulSoup4
* pandas
* pytest
* pytest-cov

---

## 📈 Hasil

* Total data mentah: ±900+ data
* Data setelah transformasi: data bersih tanpa invalid
* Test coverage: >70%

---

## 👨‍💻 Author

Project ini dibuat sebagai bagian dari submission untuk proyek akhir 'Belajar Fundamental Pemrosesan Data' dari Dicoding.

---

## 📌 Catatan

* Folder `venv`, `__pycache__`, dan file cache lainnya tidak disertakan dalam submission.
* Pastikan menjalankan project dari root directory.
