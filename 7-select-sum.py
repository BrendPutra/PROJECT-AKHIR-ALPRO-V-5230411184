import sqlite3

fauna = sqlite3.connect('database_fauna.db')
cursor = fauna.cursor()
#INSERT DATA KE TABEL

cursor.execute("SELECT SUM(jml_skrng) FROM FAUNA") # SUM PENJUMLAHAN SEMUA TOTAL POPULASI 
total_populasi = cursor.fetchone()[0] # ambil data jumlah jadikan baris baru dimulai dari indeks 0

print(f"Total Penjumlahan Semua Hewan Fanua : {total_populasi}")

fauna.close()