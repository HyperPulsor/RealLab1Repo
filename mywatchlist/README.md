# Tugas 3 Pengimplementasian Data Delivery Menggunakan Django
Rakan Fasya Athhar Rayyan - 2106750950

[Link *Web App* HTML](https://katalog-lab-rakan.herokuapp.com/mywatchlist/html/)\
[Link *Web App* XML](https://katalog-lab-rakan.herokuapp.com/mywatchlist/xml/)\
[Link *Web App* JSON](https://katalog-lab-rakan.herokuapp.com/mywatchlist/json/)

***1. Jelaskan perbedaan antara JSON, XML, dan HTML!***

Dari ketiga jenis file tersebut, terdapat dua yang merupakan *Markup Language*, yaitu HTML (*Hypertext Markup Language*)  dan XML (*JavaScript Object Notation*). *Markup Language* merupakan bahasa komputer yang biasanya menggunakan *tags* atau tanda. Akan tetapi, kedua bahasa tersebut memiliki karakteristik yang berbeda. HTML merupakan *markup language* yang menggunakan *element tree* untuk mewakilkan datanya dan dimodifikasi tampilannya sehingga menghasilkan tampilan yang kita mau. Sedangkan, XML merupakan *markup language* yang biasanya hanya digunakan untuk *data storage and delivery*. Hal ini dikarenakan XML adalah *content driven* dan HTML lebih ke *format driven*. Oleh karena itu, HTML lebih berfokus pada presentasi data. Sedangkan, XML lebih fokus pada transfer data.

JSON atau *JavaScript Object Notation* merupakan tipe *file* yang menggunakan bahasa JavaScript untuk mewakilkan data-datanya. Pada JSON ini, data direpresentasikan seperti sebuah *dictionaries* (*key* dan *value*). Dengan penggunaan *key* dan *value* ini, memudahkan untuk dibaca oleh komputer sehingga data lebih cepat untuk dibaca dan ditulis dibandingkan dengan XML dan HTML. Tidak adanya *tags* atau tanda juga mempercepat proses *read* dan *write* data. Akan tetapi, karena JSON menggunakan metode penyimpanan data yang mirip dengan *dictionaries*, maka dibandingkan dengan XML dan HTML, JSON lebih susah untuk dibaca. Selain itu, JSON mirip seperti XML yang berfokus hanya pada transfer data saehingga *content driven*.

- JSON : Dipakai karena lebih cepat untuk dilakukan *read* dan *write* dibandingkan XML dan HTML

- XML : Dipakai karena lebih mudah untuk dibaca dibandingkan JSON dan HTML

- HTML : Dipakai karena lebih mudah dimodifikasi tampilannya sehingga dipakai untuk presentasi data ke *website* dibandingkan XML dan JSON

***2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?***

*Data delivery* merupakan bagian penting dari suatu platform karena tanpa adanya implementasi ini, saat *browser* meminta data dari *database*, data tersebut bisa diambil dari *database* dan dirender menjadi sebuah output yang akan dirender pada *website*. *Data delivery* ini memungkinkan sumber datanya berupa file HTML, XML, atau JSON. Dengan mungkinnya ketiga tipe data ini, *developer* memiliki fleksibilitas terhadap input data yang akan digunakan pada *database* sehingga bisa menggunakan tipe data yang diinginkan. Digunakan tiga *format file* ini supaya memudahkan pengembang untuk melakukan modifikasi data dan *user* mudah untuk memahami data yang akan di*render*. Selain itu, saat pengembang mengubah data yang ada di *database* juga termasuk ke dalam *data delivery*.

***3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!***

- Membuat aplikasi baru bernama "mywatchlist" dengan me*run* perintah `py manage.py startapp mywatchlist`

- Membuat folder fixtures `(initial_film_data.json)` dan templates `(mywatchlist.html)` pada `mywatchlist` dan mengisi tiap folder dengan filenya masing-masing

- Melakukan *routing* dengan menambahkan mywatchlist pada `INSTALLED_APPS` di project_django `(settings.py)`. Lalu, menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada project_django `(urls.py)` supaya dapat diakses lewat `url/mywatchlist/`. Selain itu, juga menambahkan `path('html/', show_films, name='show_films')` untuk merender HTML.

- Membuat model data pada `models.py` dari `mywatchlist` dengan *field*nya masing-masing, yaitu `watched, title, rating, release_date, review` dan dipetakan pada *database* dengan menjalankan *command* `python manage.py makemigrations` dan `python manage.py migrate`

- Data-data tersebut diakses lewat `mywatchlist.html` pada folder `templates` sehingga bisa dirender dan ditampilkan di *website* oleh *user*

- Membuat *function* baru untuk menampilkan format file XML dan Json, lalu melakukan *routing* untuk setiap *function* tersebut. Penambahan `path('xml/', show_films_xml, name='show_films_xml')` dan `path('json/', show_films_json, name='show_films_json')` dilakukan di `urls.py` dari `mywatchlist`.

- Untuk *unit testing*, menambahkan tiga *function* pada `test.py` di `mywatchlist`. Tiga *function* tersebut kemudian dilakukan *testing* untuk setiap url (HTML, XML, JSON) dan dicek apakah setiap url bisa diakses dengan baik (status code dari url = HTTP_200_OK)

- Pada implementasi Postman, masukkan setiap url (HTML, XML, JSON) pada kolom *request*. Lalu, Postman akan mengembalikan hasil berupa file HTML, XML, atau JSON dari *website* beserta *status code*nya. 

<h3 align="center"> Postman HTML </h3>

![image](https://user-images.githubusercontent.com/101686378/191418832-97f3835b-d17e-488e-84eb-70bbdbd1093e.png)

<h3 align="center"> Postman XML </h3>

![image](https://user-images.githubusercontent.com/101686378/191418951-9616915c-264e-48c3-bd4d-223287f62e24.png)

<h3 align="center"> Postman JSON </h3>

![image](https://user-images.githubusercontent.com/101686378/191418694-366b7c4d-5cd0-4036-852c-811ca70063ee.png)

Referensi :

https://www.guru99.com/xml-vs-html-difference.html#:~:text=XML%20is%20abbreviation%20for%20extensible,while%20HTML%20is%20Case%20insensitive.

https://medium.com/@oazzat19/what-is-the-difference-between-html-vs-xml-vs-json-254864972bbb

https://kinsta.com/blog/xml-vs-html/

