<h1 align="left">Hi 👋! My name is Bimantyo Arya and I'm a Data Enthusiast, from Indonesia</h1>

###

<img align="right" height="150" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjNvcDI3dnFxODNkeTZwcGlscGk3N2xzNGJ0cXpzZTM0Yzl6cjdzciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OumCa12QC9CIvBe2c1/giphy.gif"  />

###
These are my Tech Stack that i used
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="30" alt="numpy logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="30" alt="pandas logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="30" alt="tensorflow logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="30" alt="docker logo"  />
</div>

###

<div align="left">
  <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="discord logo"  />
  <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="gmail logo"  />
  <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo"(https://www.linkedin.com/in/bimantyoarya/)  />
</div>

###

# Judul Project
Mental Health Analysis: Predicting Depression in Students with Machine Learning

## Repository Outline
Program ini dibuat untuk memprediksi siswa yang berpotensi mengalami depresi, sehingga dapat dilakukan tindakan preventif secara dini dan penanganan yang tepat terhadap mereka yang terindikasi mengalami gangguan kesehatan mental. Dengan bantuan model machine learning, proses identifikasi risiko depresi menjadi lebih cepat dan berbasis data, guna mendukung upaya peningkatan kesejahteraan mental siswa.

## Problem Background
Kesehatan mental merupakan isu yang semakin mendapat perhatian di era saat ini. Jika sebelumnya banyak masyarakat yang belum memahami pentingnya kesehatan mental, kini kesadaran akan hal tersebut telah meningkat secara signifikan. Kesehatan mental memengaruhi gaya hidup, pola pikir, perilaku, hingga kondisi fisik seseorang secara keseluruhan. Oleh karena itu, penting untuk mulai menyadari dan memantau kondisi mental sejak dini.

Proyek ini difokuskan untuk memprediksi potensi depresi pada siswa dengan menggunakan model machine learning, berdasarkan berbagai fitur yang tersedia dalam dataset—seperti tekanan akademik, kepuasan belajar, durasi tidur, serta faktor sosial dan psikologis lainnya.

## Project Output
Output dari project ini berupa Model Machine Learning untuk memprediksi depresi student sedari dini.

## Data
Sumber data yang digunakan berasal dari kaggle, untuk sumber data dapat dilihat di https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset. 

Dataset ini memiliki 18 kolom dan total 27.9 ribu baris data. Pada dataset ini tidak ditemukan data duplicate namun hanya terdapat missing values sebanyak 3 baris pada kolom financial_stress. Pada dataset ini terdapat beberapa professi namun berhubung profesi selain non student hanya beberapa baris data saja dan tidak mewakilkan dalam suatu populasi maka project ini berfokus pada profesi student guna menghindari outlier ataupun error, Pada kolom academic_pressure, cgpa, financial_stress, study_satisfaction terdapat nilai 0 dimana nilai tersebut bisa jadi bad input maka akan dilakukan filter menggunakan data yang legit dan valid. Mayoritas data memiliki distribusi yang normal.

## Method
Metode yang digunakan dalam project ini adalah model supervised learning dengan model KNN, SVM, Decision Tree, Random Forest dan CatBoost.

## Stacks
Untuk library yang digunakan pada program ini menggunakan bahasa pemrograman python dan untuk library menggunakan pandas, seaborn, matplotlib, scikit-learn dan cat boost

## Reference
Referensi landasan untuk project ini
- https://ayosehat.kemkes.go.id/pentingnya-kesehatan-mental-bagi-remaja
- https://hiinstitute.or.id/pentingnya-kesehatan-mental-di-era-modern-2/
- https://ejournal.fkm.unsri.ac.id/index.php/jikm/article/view/241
- https://rgrfm.tulungagung.go.id/mental-illness-penyebab-dan-dampak-yang-perlu-diketahui/

## Model Deployment
Untuk Model Deployment bisa diakses pada link dibawah. 

- Tata Cara Penggunaan
  1. Klik Link dibawah ini
  2. Kemudian pada navigation bar di samping ganti menjadi Prediction
  3. Isi data parameter sesuai dengan apa yang anda rasakan
  4. Kemudian klik Predict
  5. Model akan menampilkan hasil prediksi berdasarkan parameter yang anda isi, dan hasil akan menampilkan angka 1 jika anda terdeteksi memiliki depresi


https://huggingface.co/spaces/Bimaarya/student-depression-awareness

---
