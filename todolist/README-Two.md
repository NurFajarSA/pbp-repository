# Tugas 6: Javascript dan AJAX
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## HerokuApp Link
https://katalogku.herokuapp.com/todolist/ajax

## Async vs Sync
Pemrograman sinkronus akan mengeksekusi setiap perintah secara berurutan. Setiap eksekusi akan dijalankan setelah eksekusi sebelumnya selesai dilaksanakan. Sedangkan, pemrograman asinkronus dapat mengeksekusi perintah secara bersamaan tanpa harus menunggu suatu eksekusi selesai dijalankan.

## Event-Driven Programming
Event-driven programming merupakan sebuah paradigma pemrograman yang alurnya berdasar pada event yang dilakukan oleh antar user dan client. Ketika suatu event dijalankan, maka program akan memanggil perintah sesuai dengan event yang diterima. </br>
Pada Tugas 6 ini, penerapannya adalah `onReady` (document), `onClick`(create task button), dan `onSuccess` (post)
## Penerapan Async Pada AJAX
Penerapan pemrograman asinkrounus pada AJAX terlihat pada saat task baru dibuat website tidak perlu meng-suspend perintah lainnya selama proses AJAX berlangsung. Website akan akan terus berjalan tanpa memerlukan reload.

## Implementasi
1. Membuat views baru untuk mengimplementasikan ajax GET
2. Membuat fungsi `show_json` yang diperlukan untuk proses GET.
3. Memperbarui routing
4. Membuat modal untuk create task
5. Mengimplmentasikan ajax POST untuk membuat task baru dengan modal yang sudah dibuat
6. Membuat message success menjadi asinkronus