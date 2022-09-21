# Tugas 3 Pengimplementasian Data Delivery Menggunakan Django
Rakan Fasya Athhar Rayyan - 2106750950

[Link *Web App* HTML](https://katalog-lab-rakan.herokuapp.com/mywatchlist/html/)\
[Link *Web App* XML](https://katalog-lab-rakan.herokuapp.com/mywatchlist/xml/)\
[Link *Web App* JSON](https://katalog-lab-rakan.herokuapp.com/mywatchlist/json/)

***1. Jelaskan perbedaan antara JSON, XML, dan HTML!***

***2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?***

***3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!***

- Membuat aplikasi baru bernama "mywatchlist" dengan me*run* perintah `py manage.py startapp mywatchlist`
- Membuat folder fixtures `(initial_film_data.json)` dan templates `(mywatchlist.html)` pada `mywatchlist` dan mengisi tiap folder dengan filenya masing-masing
- Melakukan *routing* dengan menambahkan mywatchlist pada `INSTALLED_APPS` di project_django `(settings.py)`. Lalu, menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada project_django `(urls.py)` supaya dapat diakses lewat `url/mywatchlist/`. Selain itu, juga menambahkan `path('html/', show_films, name='show_films')` untuk merender html.

- Membuat model data pada `models.py` dari `mywatchlist` dengan *field*nya masing-masing, yaitu `watched, title, rating, release_date, review` dan dipetakan pada *database* dengan menjalankan *command* `python manage.py makemigrations` dan `python manage.py migrate`

- Data-data tersebut diakses lewat `mywatchlist.html` pada folder `templates` sehingga bisa dirender dan ditampilkan di *website* oleh *user*

- Membuat *function* baru untuk menampilkan format file XML dan Json, lalu melakukan *routing* untuk setiap *function* tersebut. Penambahan `path('xml/', show_films_xml, name='show_films_xml')` dan `path('json/', show_films_json, name='show_films_json')` dilakukan di `urls.py` dari `mywatchlist`.

- Untuk *unit testing*, menambahkan tiga *function* pada `test.py` di `mywatchlist`. Tiga *function* tersebut kemudian dilakukan *testing* untuk setiap url (Html, XML, Json) dan dicek apakah setiap url bisa diakses dengan baik (status code dari url = HTTP_200_OK)

- Pada implementasi Postman, masukkan setiap url (Html, XML, Json) pada kolom *request*. Lalu, Postman akan mengembalikan hasil berupa file HTML, XML, atau Json dari *website* besert *status code*nya. 

<h3 align="center"> Postman HTML </h3>

![Screenshot_340](https://user-images.githubusercontent.com/101686378/191389836-d9ddf120-c25d-4062-a403-84081f60874b.png)

<h3 align="center"> Postman XML </h3> masih salah

![Screenshot_341](https://user-images.githubusercontent.com/101686378/191389852-913e41c7-d816-44e9-9495-4c361df77fc9.png)

<h3 align="center"> Postman JSON </h3>

![Screenshot_342](https://user-images.githubusercontent.com/101686378/191389883-1500f7ee-bc89-4b78-923e-be46b4eaa590.png)
