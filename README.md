# Implementasi Interface Segregation Principle (ISP) dalam Game Tebak Angka Menggunakan Python
Proyek ini berisi sebuah permainan yang mana pengguna disuruh untuk menebak angka yang dipilih secara acak oleh program dalam rentang yang ditentukan. plikasi ini dibangun dengan menggunakan prinsip-prinsip desain perangkat lunak SOLID, khususnya Interface Segregation Principle (ISP), untuk memastikan kode yang rapi dan terstruktur.
Dalam kode permainan tebakan angka yang telah dibuat, Interface Segregation Principle (ISP) diterapkan dengan cara memisahkan antarmuka menjadi dua bagian utama: Game dan GameStatistics.
Interfaces Game berfokus pada logika dasar permainan, menyediakan method seperti start(self)untuk memulai permainan dan start(self, number:int)untuk menerima dan memproses tebakan dari pengguna. Interfaces ini dirancang agar hanya berisi method yang relevan untuk mengelola permainan itu sendiri.
Di sisi lain, interfaces GameStatistics dirancang khusus untuk menangani kebutuhan terkait statistik permainan, seperti jumlah tebakan yang telah dilakukan get_attempts(self) dan hasil dari tebakan terakhir get_last_result(self). Dengan memisahkan metode statistik ini ke dalam antarmuka yang berbeda, kita memastikan bahwa kelas yang hanya membutuhkan logika permainan tidak dipaksa untuk mengimplementasikan metode statistik, dan sebaliknya.
Implementasi kedua antarmuka ini dalam kelas NumberGuessingGame() memastikan bahwa kelas ini memenuhi kontrak dari kedua antarmuka tersebut, tanpa perlu menambahkan metode yang tidak relevan dengan fungsionalitas inti dari permainan atau statistik. Kelas ini bertanggung jawab untuk mengelola logika permainan serta menyediakan statistik yang dibutuhkan, namun dengan tanggung jawab yang jelas dan terpisah sesuai dengan antarmuka yang telah didefinisikan.
Dengan demikian, penerapan ISP dalam kode ini menjamin bahwa antarmuka tetap sederhana, fokus, dan tidak memaksa implementasi yang berlebihan, yang selanjutnya menjaga kode agar tetap modular, mudah dipelihara, dan scalable.


# Fitur Aplikasi
1. Pemain memulai permainan dengan meng-input angka
2. Jika angka yang di-input lebih besar atau lebih kecil, permainan akan berlanjut
3. Pemain akan terus menebak angka hingga menemukan angka yang tepat
