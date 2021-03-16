# List 10 teman
list = ['Bagus','Rio','Gea','Ara','Sasa','Rizal','Iqbal','Reza','Alif','Dito']

# Menampilkan list indeks nomor 4,6, dan 7
print("List indeks nomor 4,6, dan 7 adalah",list[4],",",list[6],", dan",list[7])

# Mengganti nama teman di list 3,5, dan 9
list[3] = 'Cancan'
list[5] = 'Arya'
list[9] = 'Rizky'

# Menambahkan 2 nama teman
list.append('Ayu')
list.append('Rara')

# Menampilkan semua teman dengan pengulangan
print(list*2)

# Menampilkan panjang list
print(len(list))