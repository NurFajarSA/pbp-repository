# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## HerokuApp Link
https://katalogku.herokuapp.com/todolist

###  Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
apa hayo

#### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form> `secara manual.
apa hayo

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
apa hayo

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
    - Sudah