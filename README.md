# tugas-struktur-data-3

# Praktikum Struktur Data 

Repository ini berisi solusi Python untuk 5 soal praktikum algoritma sorting, searching, dan counting.

## Daftar Soal

### Soal 1: Modified Binary Search
Mengimplementasikan fungsi `countOccurrences` untuk menghitung jumlah kemunculan elemen dalam list terurut.
- **Kompleksitas:** $O(\log n)$
- **Metode:** Menggunakan dua kali binary search (satu untuk mencari indeks kiri pertama, satu untuk indeks kanan terakhir).

### Soal 2: Bubble Sort dengan Analisis Langkah
Modifikasi Bubble Sort untuk mengembalikan tuple `(sorted_list, comparisons, swaps, passes)`.
- **Fitur:**
  - Early termination (berhenti jika tidak ada swap dalam satu pass).
  - Mencetak state array setelah setiap pass.
- **Analisis:** Pada input yang sudah terurut `[1, 2, 3, 4, 5]`, algoritma hanya membutuhkan 1 pass karena flag `swapped` tetap False, sedangkan input acak membutuhkan $N$ pass.

### Soal 3: Hybrid Sort
Fungsi `hybridSort` yang memilih algoritma berdasarkan panjang array (`threshold`).
- **Logika:**
  - Jika `len(arr) < threshold`: Gunakan **Insertion Sort**.
  - Jika `len(arr) >= threshold`: Gunakan **Selection Sort**.
- **Catatan:** Biasanya Hybrid Sort menggabungkan Merge/Quick Sort dengan Insertion Sort. Namun sesuai soal, kita membandingkan efisiensi Insertion vs Selection pada berbagai ukuran data. Insertion Sort umumnya lebih efisien untuk data kecil karena pergeseran elemen lebih sedikit dibanding swap pada Selection Sort.

### Soal 4: Merge Tiga Sorted Lists
Menggabungkan 3 list terurut menjadi satu dalam waktu $O(n)$.
- **Metode:** Menggunakan 3 pointer (`i, j, k`) untuk melacak posisi di masing-masing list. Pada setiap iterasi, kita membandingkan nilai di ketiga pointer dan mengambil nilai terkecil untuk dimasukkan ke list hasil.
- **Constraint:** Tidak boleh memanggil fungsi merge 2-list secara bertahap (harus 1 pass).

### Soal 5: Inversions Counter
Menghitung jumlah pasangan indeks $(i, j)$ di mana $i < j$ tetapi $arr[i] > arr[j]$.
1. **Naive Approach:** Brute force dengan nested loop. Kompleksitas $O(n^2)$.
2. **Smart Approach:** Modifikasi Merge Sort. Saat proses merge, jika elemen dari sub-array kanan diambil sebelum sub-array kiri habis, maka sisa elemen di kiri membentuk inversi dengan elemen kanan tersebut. Kompleksitas $O(n \log n)$.
3. **Hasil:** Pendekatan Merge Sort jauh lebih cepat pada data besar (10.000 elemen) karena pertumbuhan waktunya jauh lebih lambat dibanding kuadratik.

## Cara Menjalankan

1. Pastikan Python sudah terinstall.
2. Simpan kode utama sebagai `Latihan Soal 1-5.py`.
3. Jalankan melalui terminal:
   ```bash
   python praktikum_algoritma.py
   ```

## Struktur Kode
- `countOccurrences`: Binary Search modifikasi.
- `bubbleSort`: Sorting dengan tracking statistik.
- `hybridSort`, `insertion_sort_count`, `selection_sort_count`: Perbandingan algoritma sorting.
- `mergeThreeSortedLists`: Merge 3 list simultan.
- `countInversionsNaive`, `countInversionsSmart`: Penghitung inversi.
