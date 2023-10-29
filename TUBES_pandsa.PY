#kamus
#int: sum_global, i,

from tabulate import tabulate
import pandas as pd
data = pd.read_csv("data.csv")
rows_data = len(data)

sum_global = 0
arr_temporary = [[" " for i in range (2)]for j in range (rows_data)]
# arr_keranjang = [[" " for i in range (999)]for j in range (3)]
arr_keranjang = [[" " for i in range (3)]for j in range (999)]



def binserfirst(low, high, key):
    index = 1
    while low <= high:
        mid = int(low + ((high-low)/2))
        if data['category'][mid] < key:
            low = mid + 1
        elif data['category'][mid] > key:
            high = mid - 1
        elif data['category'][mid] == key:
            index = mid
            high = mid - 1
    return index

def binserlast(low, high, key):
    index = 1
    while low <= high:
        mid = int(low + ((high-low)/2))
        # print(mid)
        # print(low, high)
        # print (data['category'][mid])
        if data['category'][mid] < key:
            low = mid + 1
        elif data['category'][mid] > key:
            high = mid - 1
        elif data['category'][mid] == key:
            index = mid
            low = mid + 1
    return index

def count(harga):
    N = int(input("Mau pesen berapa banyak? "))
    arr_keranjang [i][1] = str(N)
    arr_keranjang [i][2] = str(N * harga)
    return N*harga

def process(x,len):
    for loop in range(len):
        print(str(loop+1) + ". " + x[loop][0] + " (" + str(x[loop][1]) + "k)")
    N = int(input("Masukkan menu yang Anda inginkan: "))
    while(N < 1 or N > len):
        N = int(input("Masukkan menu yang Anda inginkan: "))
    #proses barang
    arr_keranjang[i][0] = x[N-1][0]

    #proses harga
    num = (x[N-1][1])
    count(num)



tempat_makan = 0
str_tempat_makan = " "
while (tempat_makan < 1) or (tempat_makan > 2):
    tempat_makan = int(input("""
Pilih opsi tempat makan:
1. makan disini
2. bawa pulang
input angka:
"""))
if tempat_makan == 1:
  str_tempat_makan = "makan disini"
elif tempat_makan == 2:
  str_tempat_makan = "bawa pulang"


boolpesan = True
i = 0

while (boolpesan == True):
    print("""
Berikut kategori menu:
1. Promosi
2. Burger dan nuggets
3. Ayam
4. Happy meal
5. Paket keluarga
6. Menu receh
7. Camilan
8. Minuman
9. Pencuci mulut
10. Nasi
    """)
    masukan = int(input("Silakan pilih kategori menu: "))
    start = binserfirst(0,rows_data,masukan)
    finish = binserlast(0,rows_data,masukan)
    increase = 0
    while(start <= finish):
        arr_temporary[increase][0] = data['item'][start]
        arr_temporary[increase][1] = data['price'][start]
        increase += 1
        start += 1
    process(arr_temporary,increase)

    batal = str(input("Mau batal pemesanan tidak? (y/n): "))
    if (batal == 'y' or batal == 'Y'):
        del arr_keranjang[i][0:3]

    else:
        sum_global += float(arr_keranjang [i][2])
    
    konfirmasi = str(input("Mau pesen lagi ga? (y/n): "))
    if (konfirmasi == 'n' or konfirmasi == 'N'):
        boolpesan = False
    elif (konfirmasi == 'y' or konfirmasi == 'Y'):
        boolpesan = True
        i += 1


ambil_makan = 0
str_ambil_makan = " "

while ambil_makan < 1 or ambil_makan > 2:
    ambil_makan = int(input("""
pilih opsi pengambilan makan:
1. Diantar ke meja
2. Diambil ke konter
input angka:
"""))
no = 0
if ambil_makan == 1:
    str_ambil_makan = "Diantar ke meja"
    no = int(input('Masukkan nomor meja: '))
elif ambil_makan == 2:
    str_ambil_makan = "Diambil ke konter"
    no = int(input('Masukkan nomor pesanan: '))


print(f"""



----------------------------------------------------------------
              STRUK PEMBAYARAN PEMESANAN MAKANAN
----------------------------------------------------------------
tempat makan: {str_tempat_makan}
pengambilan: {str_ambil_makan}
No: {no}
         """)


out_data = arr_keranjang[0:i+1]
out_header = ["Item","Jumlah","Price"]
print(tabulate(out_data,out_header,tablefmt="plain"))

# out = pd.DataFrame(data = arr_keranjang)
# out = out.rename(columns={0: 'jumlah', 1 : 'item', 2: 'total price'})
# print(out.iloc[0:i+1])

# for column in range (i+1):
#   for row in range (3):
#     print(arr_keranjang[row][column], end="   ")
#   print(" ")

print(" ")
print (f"Total harga: {sum_global}k")
