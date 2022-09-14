# Tugas 2 Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django
Rakan Fasya Athhar Rayyan - 2106750950

[Link *Web App*](https://katalog-lab-rakan.herokuapp.com/) (Tambahkan /katalog setelah url)

***1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;***

![Bagan PBP (1)](https://user-images.githubusercontent.com/101686378/190063578-44c35105-7489-4e35-bf2f-9c1891ed087e.png)


Pertama, *user* akan meminta *request* kepada framework Django untuk mengambil *resource* yang dibutuhkan untuk *website*. Lalu, *framework* akan berperan sebagai pengatur untuk mengcek apakah *resource* tersebut ada di URL (**urls.py**). Setelah itu, URL akan memanggil View (**views.py**) yang akan berinteraksi dengan Model (**models.py**) dan Template (**html**) (**Hanya View yang dapat mengakses Model dan Template**). Kemudian, View akan berinteraksi dengan Model berupa suatu *query* dan *database* akan mengembalikan hasil yang berisi data-data (respon) ke Views kembali lewat Model. Selain itu, Views juga dapat memodifikasi data-data pada Model dengan *query*. Setelah *request* berhasil diproses, Views akan mengakses Template dan menggunakan hasil tadi untuk dipetakan pada Template yang nantinya akan berperan sebagai output untuk user setelah dirender. Kemudian, output berupa HTML yang sudah dirender tersebut akan dikembalikan ke Views dan akan diteruskan hingga ke *user* untuk diperlihatkan.

<!-- Kaitannya :
**urls.py** akan mengecek *resources* yand dibutuhkan dari *user request* pada **views.py**. **views.py** ini menjadi perantara utama antara **models.py** dan berkas file html. Hal ini dikarenakan **models.py** tidak dapat secara langsung mengakses berkas dan sebaliknya. **views.py** akan berinteraksi dengan **models.py** untuk mendapatkan data-data yang dibutuhkan berdasarkan *user request* atau mengedit data yang sudah ada pada **models.py**. Kemudian, **models.py** akan mengembalikan data-data yang dibutuhkan untuk *request*. Tetapi, Template hanya bisa mengakses *query* tersebut lewat View. Setelah output selesai dibuat, output akan dikembalikan ke views.py dan kemudian dikembalikan lewat urls.py serta framework Django hingga sampai ke *user* sebagai bentuk respon. -->

***2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?***

Virtual environment digunakan supaya setiap proyek Django memiliki lingkungan dengan *dependencies* yang berbeda-beda. Hal ini akan mencegah terjadinya konflik pada Django, seperti versi Django yang berbeda pada komputer kita. Fungsi dari penggunaan venv adalah untuk mengisolasi *package* dan *dependencies* untuk suatu proyek tertentu. Jika tidak menggunakan *virtual environment*, maka *package* dan *dependencies* akan terinstall pada *global environment* di komputer kita. Hal ini menyebabkan mungkin terjadinya konflik versi karena berbeda. Selain itu, update *package* dan *dependencies* akan mengubah data pada penyimpanan lokal komputer kita sehingga dapat menyebabkan perbedaan data tersebut.

Walaupun terdapat resiko - resiko tersebut, untuk membuat suatu aplikasi web berbasis Django dapat tidak menggunakan *virtual environment*. Akan tetapi, banyak resiko yang harus dihadapi.

***3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.***

#### Poin 1 : views.py
View mengambil data dari *database* lewat Model (models.py). Selain mengambil, view jugamemodifikasi *database* dengan menambahkan beberapa variabel, seperti Nama dan NPM. Kedua variabel tersebut disimpan pada context yang merupakan dictionary. Setelah function show_katalog dipanggil, maka context akan dirender dan ditampilkan pada halaman HTML *website*.

 #### Poin 2 : urls.py
 URL (urls.py) akan melakukan routing terhadap fungsi show_katalog. Routing mengambil path dari katalog yang sudah didaftarkan pada urls.py dalam project_django. Oleh karena rutenya yaitu "katalog/", maka untuk diakses di website perlu menambahkan "\katalog" setelah url dari websitenya supaya bisa mengakses HTML yang sudah dirender. Selain itu, juga menjalankan function show_katalog untuk ditampilkan di HTML. 
 
 #### Poin 3 : katalog.html
 Pada katalog.html yang berada di folder templates dilakukan for loop terhadap list-list barang yang sudah di load dari initial_catalog_data.json. Data-data tersebut akan disimpan pada list_barang.
 
  #### Poin 4 : Deploy App
  Menambahkan HEROKU_APP_NAME dan HEROKU_API_KEY pada Github Secrets. Hal ini supaya kita bisa menyambungkan Heroku dengan Repo Github kita. Setelah menambahkan kedua secrets tersebut, maka tinggal mengecek di Github Actions untuk deploy.