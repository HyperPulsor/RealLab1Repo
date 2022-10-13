# Tugas 6: Javascript dan AJAX
Rakan Fasya Athhar Rayyan - 2106750950

Kontributor :

*Andi Muhamad Dzaky Raihan - 2106631412*

*Fauziah Putri Fajrianti - 2106707435*

[Link *Web App* Todo-list](https://katalog-lab-rakan.herokuapp.com/todolist/login/?next=/todolist/)

***1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming***

Syncronous programming dapat membuat program akan menjalankan perintah berdasarkan urutan yang ditentukan oleh instruksi. Program akan menunggu sampai suatu kegiatan tertentu selesai dilakukan sebelum melakukan kegiatan lain. Asynchronous programming membaut program akan menjalankan perintah-perintah secara bersamaan.

***2.  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.***

Paradigma Event-Driven Programming merupakan suatu paradigma yang didasarkan pada kemunculan event. Kemunculan tersebut akan memengaruhi alur kontrol dari program. Dengan paradigma ini, suatu program akan mendeteksi suatu event, mengeksekusi event handler yang telah dihandle, dan menggunakan callback methods. Contohnya adalah saat menambahkan task dengan AJAX. Pada function `addNewTask()` yang menggunakan method POST. Function ini menerima data dari form dari modal yang sudah dihandle eventnya dengan onclick yang ada di button submit saat diklik. 

***3. Jelaskan penerapan asynchronous programming pada AJAX.***

Asynchronous programming pada AJAX terjadi pada saat server mengambil dan mengirim data. Kegiatan ini terjadi di belakang layar. Oleh karena itu, website tidak perlu refresh atau reload halaman untuk memperbarui data yang sudah diubah. Callback akan dikirim oleh AJAX dalam bentuk event-driven programming supaya terjadi secara sinkronus. AJAX POST dan GET akan membuat function yang menggunakan kedua method tersebut untuk ditangkap oleh event-handler yang sudah dibuat.

***4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.***

- Fungsi `show_json` dibuat untuk return data input form dalam bentuk JSON
- Membuat routing `/todolist/json` pada `urls.py` untuk fungsi `show_json`
- Membuat fungsi JavaScript `cardReset()` yang methodnya GET untuk merender cards berdasarkan database JSON dari `/todolist/json`.
- Apabila halaman sudah selesai dimuat, akan melakukan fungsi `cardReset()` untuk render cards
- Membuat fungsi `add_task_ajax` dan routing `/todolist/add` pada `urls.py`
- Membuat modal yang merupakan suatu form untuk input nama dan deskripsi task sehingga cards bisa ditambah
- Membuat fungsi JavaScript `addNewTask()` dengan tipe method POST untuk menerima input dari modal dan disubmit. Lalu, input tersebut akan diproses oleh `add_task_ajax`. Setelah diproses, maka website akan update cards secara asinkronus.