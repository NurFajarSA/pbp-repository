# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## HerokuApp Link
https://katalogku.herokuapp.com/todolist

###  Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Penggunaan `{% csrf_token %}` bertujuan untuk melindungi web dari serangan Cross Site Request Forgery. CSRF token bekerja dengan mengirimkan token ke client yang kemudian akan dikirimkan kembali pada request selanjutnya. Apabila token tidak sesuai, maka request akan direject. Oleh karena itu, apabila tidak ada potongan kode tersebut pada elemen form, maka akan sangat rentan dari serangan CSRF.

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form> `secara manual.
Ya, kita dapat membuat elemen `<form>` secara manual. Pembuatan elemen `<form>` secara manual dapat dilakukan dengan cara menggunakan elemen `<input>` dan menyesuaikan dengan kebutuhan form yang ada di code django.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika client memasukan input task baru dan menekan button Create, maka button tersebut akan mengirimkan request POST. `views.py` akan memvalidasi request dan data yang ada, lalu menyimpan data tersebut di database. Setelah itu, `views.py` akan melakukan redirect ke laman show_tasks. Laman show_tasks akan mengambil semua data task client yang ada di database dan menampilkannya kembali.

## Implementasi
1.  Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
    - run `python manage.py startapp todolist` dan masukan di variable list INSTALLED_APP

2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
    - Tambah url di file `urls.py` pada project_django

3. Membuat sebuah model Task
    - Membuat model Task pada file `models.py` sesuai dengan ketentuan atribut pada soal

4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
    - Mengimplemetasikan fitur ini dengan bantuan `django.contrib.auth`

5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
    - Membuat fungsionalitas `show_tasks`, `update`, `delete` pada `views.py`. 

6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
    - Membuat model form di `forms.py` kemudian mebuat fungsionalitasnya (`create_task`) pada `views.py`

7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:
    - Menambangkan path `show_tasks`, `create_task`, `update`, `delete` di `urls.py` 

8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - Deploy seperti biasa

9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
    - username: user1 password: 29Nda9qEcvB7x2a
    - username: user2 password: 2JFiixkBnn2MDRm