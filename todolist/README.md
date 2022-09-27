# Tugas 4 Pengimplementasian Form dan Autentikasi Menggunakan Django
Rakan Fasya Athhar Rayyan - 2106750950

[Link *Web App* Todo-list](https://katalog-lab-rakan.herokuapp.com/todolist/login/?next=/todolist/)

***1.  Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?***

`{% csrf_token %}` merupakan token unik yang dibuat untuk setiap *user session* dan berisi *value* yang bersifat rahasia dan tidak dapat diprediksi. Token ini berguna untuk mencegah dari terjadinya *CSRF (Cross-Site Request Forgery) Attack*. Pada `<form>`, akan terdapat dua token yang dibuat, yaitu pada saat pengguna memasuki laman `<form>` dan setelah dikembalikan *request* dari pengguna saat mensubmit data yang dibutuhkan `<form>`. Lalu, kedua token tersebut akan dibandingkan. Apabila salah satu token tidak ada atau memiliki value yang berbeda, maka *request* tersebut akan ditolak dan sesi user akan dihapus serta dicatat pada log sebagai potensi *CSRF Attack*.

Pada `<form>` yang tidak memiliki `{% csrf_token %}`, maka akan muncul *error* `Forbidden (403) CSRF verification failed. Request aborted`. Oleh karena itu, dibutuhkan `{% csrf_token %}` untuk setiap `<form>` yang dibuat pada suatu website.

***2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.***

Elemen form dapat dibuat tanpa menggunakan generator `{{ form.as_table }})`. Alternatifnya adalah membuat form dengan cara manual. Form ini dapat dibuat dengan menggunakan method `POST`. Selain itu, juga dibutuhkan `{% csrf_token %}`. Untuk membuat suatu form manual, pertama harus membuat tag input dan form yang dibutuhkan pada HTML. Tag form berfungsi supaya dibaca oleh html sebagai suatu form. Input ini memiliki banyak tipe, tetapi untuk suatu form hanya membutuhkan tipe text (input pengguna) dan submit (submit data dari input pengguna). Setelah pengguna menekan input submit yang berupa tombol, maka input text yang sudah diisi oleh pengguna akan disubmit ke *server*.

***3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.***

Awalnya, pengguna memasukan data pada form HTML yang telah dirender dan disubmit dengan menekan tombol submit. Lalu, pada `views.py` *function* yang berperan dalam mengakses form, akan mengolah data-data tersebut. Apabila hanya mengubah bagian dari data yang sudah ada, maka data hanya disimpan pada database. Sedangkan, apabila memasukkan data baru yang belum ada di *database*, maka akan dibuat objek baru yang akan disimpan pada *database*. Setelah itu, data-data yang akan diakses pada HTML dapat diakses setelah dilakukan proses *rendering*.

***4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.***

- Menjalankan *command* `python manage.py startapp todolist` pada *virtual environment* folder
- Menambahkan `path('todolist/', include('todolist.urls'))` pada project_django di urls.py untuk *routing* terhadap `todolist` sehingga dapat mengakases `http://localhost:8000/todolist`
- Memetakan *model* dalam *database* sesuai data yang ditugaskan pada `models.py` di folder `todolist`.
- Membuat fungsi-fungsi yang diperlukan untuk login, logout, dan register pada `views.py` di folder `todolist`. Lalu, membuat `login.html` dan `register.html` pada folder templates supaya bisa dilihat oleh pengguna. Selain itu, perlu ditambahkan `@login_required(login_url='/todolist/login/')` pada fungsi yang menampilkan `todolist` dan menambahkan *task* pada `todolist` supaya hanya bisa diakses setelah melakukan login.
- Pada HTML halaman utama `todolist`, ditampilkan *username* pengguna dengan mengakses variabel `{{username}}` yang telah dirender. Kemudian, membuat tabel dengan tag `<table>` dan dua tombol untuk tambah *task* baru dan *logout*. Tabel akan menampilkan data-data *task* yang sudah disubmit oleh pengguna ke *database*.
- Membuat form pada `add.html` dengan *tag* `<form>` yang mengambil input dari pengguna berupa nama dan deskripsi dari *task* dengan *redirect* url `todolist/create-task` lewat tombol tambah *task* baru. Setelah tombol dipencet, maka form akan dikirim ke *server* dan diakses oleh fungsi `add_task` di `views.py` supaya bisa disimpan pada *database*. 
- Menambahkan path yang dibutuhkan sesuai fungsinya masing-masing pada `urls.py` pada `todolist`.
- Menambahkan kondisional dengan atribut `is_finished` yang merubah *status* dari task supaya yang ditampilkan adalah `Selesai` atau `Belum Selesai`. Lalu, membuat tombol untuk menghapus task yang ada di `todolist` dengan menghapus data yang ada di *database*.
- Deploy *website* ke Heroku dan membuat dua pengguna dengan tiga *task*nya masing-masing. 


