import sqlite3
fauna = sqlite3.connect('database_fauna.db')

# INSERT DATA KE TABLE
fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Harimau','Mamalia','Jawa','40','2019')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Kuskus','Mamalia','Sulawesi','30','2021')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Beruang Madu','Mamalia','Sumatera','1000','2020')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Pesut Mahakam','Mamalia','Kalimantan','100','2021')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Burung Maleo','Burung','Sulawesi','7000','2023')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Macan Dahan','Mamalia','Sumatera','400','2020')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Kancil','Mamalia','Jawa','60','2022')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Gajah Kalimantan','Mamalia','Kalimantan','1500','2021')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Elang Jawa','Burung','Jawa','200','2021')
               ''')

fauna.execute(f'''
               INSERT INTO FAUNA(nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
               VALUES('Katak Borneo','Amfibi','Kalimantan','2000','2023')
               ''')

fauna.commit()
fauna.close()