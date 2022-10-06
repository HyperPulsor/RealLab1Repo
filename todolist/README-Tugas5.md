# Tugas 5 Web Design Using HTML, CSS, and CSS Framework
Rakan Fasya Athhar Rayyan - 2106750950

[Link *Web App* Todo-list](https://katalog-lab-rakan.herokuapp.com/todolist/login/?next=/todolist/)

***1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?***

- **Inline CSS**

Merupakan kode CSS yang langsung ditulis pada tag suatu elemen HTML. Dengan menggunakan metode ini, secara tidak langsung proses *request* HTTP lebih cepat sehingga *load* website juga lebih cepat. Akan tetapi, penggunaan *Inline CSS* ini memakan waktu dan tidak efisien karena kita harus memasukkan kode CSS ke masing-masing tag yang ingin kita *styling*.

- **Internal CSS**

Merupakan kode CSS yang ditulis di dalam tag `<style>` pada `<header>` pada HTML yang ingin kita ubah. Dengan menggunakan metode ini, kita dapat dengan mudah membuat *styling* yang berbeda-beda untuk setiap *page* pada *website* (hanya berlaku pada satu page tertentu). Selain itu, kita hanya perlu menggunakan file HTML yang sudah ada *styling*nya tanpa perlu mengupload *file* CSS di `static` folder. Akan tetapi, penggunaan *Internal CSS* membuat *website* menjadi lambat karena *website* harus load setiap *page* yang memiliki *style* berbeda-beda.

- **External CSS**

Merupakan kode CSS yang ditulis tidak dalam file HTML. Kode ini ditulis dalam file terpisah dengan tipe file `.css`. File ini nantinya akan ditaruh di `static` folder pada proyek. Dengan menggunakan metode ini, kita dapat membuat file HTML memiliki ukuran yang lebih kecil dan rapih. Selain itu, *load* *website* juga lebih cepat dan penggunaan file ini dapat digunakan dalam beberapa halaman juga dan dipakai secara sekaligus. Akan tetapi, file CSS dapat membuat *page* menjadi berantakan karena tidak berhasil di*load* oleh *website* karena koneksi internet yang lambat.

***2.  Jelaskan tag HTML5 yang kamu ketahui!***

`<div>`         : menspesifikasikan suatu bagian tertentu

`<h1>`-`<h6>`   : tulisan *headings* dari html (1 paling besar ukurannya)

`<head>`        : mendefinisikan bagian *head*

`<body>`        : mendefinisikan bagian badan

`<footer>`      : mendefinisikan bagian bawah (*footer*) dari HTML

`<button>`      : membuat suatu button yang bisa dipencet

`<p>`           : mendefinisikan suatu bagian paragraf teks

`<a>`           : menambahkan link pada HTML

`<link>`        : menambahkan path pada HTML

`<style>`       : menambahkan *styling* untuk elemen HTML lain

***3.  Jelaskan tipe-tipe CSS selector yang kamu ketahui.***

- Universal Selector

Merupakan *selector* untuk meng*include* semua elemen HTML. Biasanya digunakan untuk mengubah semua elemen pada HTML seperti *reset*.

- Type Selector

Merupakan *selector* yang memasukkan semua elemen yang memiliki nama sama. Biasanya digunakan untuk mengubah *styling* hanya pada satu elemen tertentu.

- Class Selector

Merupakan *selector* yang memasukkan semua elemen yang memiliki nama class yang sama. Dibuat dengan memasukkan tanda titik didepan lalu nama classnya.

- Id Selector

Merupakan *selector* yang memasukkan semua elemen dengan Id yang sama. Id sifatnya unik. Dibuat dengan memasukkan `#` lalu Idnya.

- Attribute Selector

Merupakan *selector* yang memasukkan semua elemen dengan atribut yang sama. Ini mirip dengan Class Selector.

***4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas***
- Import Boostrap ke project `todolist` dengan memasukkan link Boostrap ke setiap file HTML yang akan digunakan pada bagian `<head>` dan `<body>` HTML (link pada `<head>` dan script pada `<body>`)
```
<link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"
    rel="stylesheet"
    integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT"
    crossorigin="anonymous"
  />
<script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
    crossorigin="anonymous"
  ></script>
```
- Melakukan kustomisasi pada bagian login, register, dan create-task dengan menggunakan *card*, *button*, dan *font*.
- Untuk *responsive*, saya menggunakan `flex` yang diberikan `-lg` atau penggunaan *grid system* atau elemen lain yang *responsive* dengan commadn seperti `-lg` supaya *resize* relatif terhadap ukuran layar.
- Melakukan kustomisasi untuk todolist dengan menggunakan cards dari Boostrap. Cards dibuat dengan *grid system* yaitu baris dan kolom supaya rapih. Lalu, juga implementasi hover pada `<style>` di `<head>`. Selain itu, juga implementasi elemen lain seperti navbar, button, background image.
- *Responsiveness* dapat dicek dengan *inspect element* yang ada di Google Chrome (dilihat dari berbagai jenis resolusi);.