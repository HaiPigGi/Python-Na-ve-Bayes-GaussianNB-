Berikut adalah penjelasan langkah-langkah dalam kode tersebut:

Langkah 1: Load dataset

Dataset "bank.csv" dibaca menggunakan library Pandas dan disimpan dalam variabel data.
Langkah 2: Preprocessing data

Kolom-kolom kategorikal pada dataset diisi dengan nilai "unknown" menggunakan metode fillna() untuk mengatasi nilai yang hilang.
LabelEncoder digunakan untuk mengubah nilai-nilai kategorikal menjadi angka.
Langkah 3: Pembagian dataset

Dataset dibagi menjadi data training dan data testing menggunakan train_test_split() dari library scikit-learn. Data testing sebesar 20% dari keseluruhan dataset.
Langkah 4: Melatih model Naïve Bayes

Model klasifikasi Naïve Bayes (GaussianNB) dibuat menggunakan library scikit-learn (sklearn).
Model dilatih menggunakan data training.
Langkah 5: Melakukan prediksi

Model yang telah dilatih digunakan untuk melakukan prediksi pada data testing.
Langkah 6: Evaluasi model

Metrik evaluasi seperti akurasi (accuracy), presisi (precision), dan recall dihitung menggunakan library scikit-learn (sklearn.metrics).
Membuat GUI menggunakan Tkinter

Sebuah jendela GUI dibuat menggunakan Tk().
Label-label dibuat untuk menampilkan output hasil evaluasi model.
Frame dibuat untuk menampilkan plot.
Plot bar digunakan untuk menampilkan skor evaluasi dalam bentuk grafik batang.
Canvas digunakan untuk menampilkan plot di dalam frame.
Tombol "Close" digunakan untuk menutup jendela GUI.
Menjalankan GUI

GUI window dijalankan menggunakan window.mainloop().
Dengan menjalankan kode di atas, Anda akan melihat sebuah jendela GUI yang menampilkan hasil evaluasi model Naïve Bayes (akurasi, presisi, recall) dan grafik batang yang merepresentasikan skor evaluasi tersebut.

Pastikan file "bank.csv" tersedia di direktori yang sama dengan file Python tersebut, dan juga pastikan Anda telah menginstal library yang diperlukan seperti Pandas, Tkinter, scikit-learn, dan matplotlib sebelum menjalankan kode tersebut.