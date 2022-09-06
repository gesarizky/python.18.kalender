# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Mengimpor Modul Calendar
import calendar

# Menginput Tahun dan Bulan
yy = int(input("Masukkan Tahun: "))
mm = int(input("Masukkan Bulan: "))

# Menampilkan Kalender Bulanan
print(calendar.month(yy, mm))
