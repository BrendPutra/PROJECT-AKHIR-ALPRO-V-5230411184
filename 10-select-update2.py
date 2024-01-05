import sqlite3
#select all data fauna
fauna = sqlite3.connect('database_fauna.db')

cursor = fauna.cursor()

#ubah berdasarkan id_fauna
id_fauna = 4


#mengambil semua data dalam tabel dan ditampilkan
cursor.execute(f"UPDATE FAUNA SET asal = 'Kalimantan Timur' WHERE id_fauna = {id_fauna}")
fauna.commit()

#tampilkan data dalam bentuk baris
baris_tabel = cursor.fetchall()

# membuat format table dengan method format()
print(" TABEL FAUNA")
print("="*110)
print("{:<10}{:<21}{:<18}{:<17}{:<20}{:<20}".format("ID FAUNA","NAMA FAUNA","JENIS","ASAL","JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
print("="*110)

# tampilkan data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<11}{:<20}{:<17}{:<20}{:<21}{:<22}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5],))

fauna.close