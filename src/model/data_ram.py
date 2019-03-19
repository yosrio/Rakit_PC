import pymysql

con = pymysql.connect(db="komponen_komputer", user="root", passwd="",
                  host="localhost", port=3306, autocommit=True)
nama_ram = con.cursor()
nama_ram.execute("SELECT nama_ram FROM ram;")
tipe_ram = con.cursor()
tipe_ram.execute("SELECT tipe_ram FROM ram;")
ukuran_ram = con.cursor()
ukuran_ram.execute("SELECT ukuran_ram FROM ram;")
jumlah_ram = con.cursor()
jumlah_ram.execute("SELECT jumlah_ram FROM ram;")
total_ukuran_ram = con.cursor()
total_ukuran_ram.execute("SELECT total_ukuran_ram FROM ram;")
seri = con.cursor()
seri.execute("SELECT seri FROM ram;")
speed = con.cursor()
speed.execute("SELECT speed FROM ram;")
harga = con.cursor()
harga.execute("SELECT harga FROM ram;")

namaStr = nama_ram.fetchall()
tipe_ramStr = tipe_ram.fetchall()
ukuran_ramInt = ukuran_ram.fetchall()
jumlah_ramInt = jumlah_ram.fetchall()
total_ukuran_ramInt = total_ukuran_ram.fetchall()
seriStr = seri.fetchall()
speedInt = speed.fetchall()
hargaInt = harga.fetchall()

listNama_ram = []
listTipe_ram = []
listUkuran_ram = []
listJumlah_ram = []
listTotal_memori_ram = []
listSeri_ram = []
listSpeed_ram = []
listHarga_ram = []

def strip_non_ascii(string):
    stripped = (c for c in string if ord(c) != 44 and ord(c) != 40 and
                ord(c) != 41 and ord(c) != 39)
    return ''.join(stripped)

def getDataRam():
    i=0
    while i<len(namaStr):
        str1 = str(namaStr[i])
        str2 = str(tipe_ramStr[i])
        str3 = str(ukuran_ramInt[i])
        str4 = str(jumlah_ramInt[i])
        str5 = str(total_ukuran_ramInt[i])
        str6 = str(seriStr[i])
        str7 = str(speedInt[i])
        str8 = str(hargaInt[i])
        
        listNama_ram.append(strip_non_ascii(str1))
        listTipe_ram.append(strip_non_ascii(str2))
        listUkuran_ram.append(int(strip_non_ascii(str3)))
        listJumlah_ram.append(int(strip_non_ascii(str4)))
        listTotal_memori_ram.append(int(strip_non_ascii(str5)))
        listSeri_ram.append(strip_non_ascii(str6))
        listSpeed_ram.append(int(strip_non_ascii(str7)))
        listHarga_ram.append(int(strip_non_ascii(str8)))
        i=i+1

def showRam():
    getDataRam()
    j=0
    while j<len(listNama_ram):
        print("==============================")
        print("Nama: ",listNama_ram[j],"\nTipe Ram: ",listTipe_ram[j],"\nSize: ",
                listUkuran_ram[j],"\nJumlah Ram: ",listJumlah_ram[j], "\nTotal Ukuran:", listTotal_memori_ram[j],
                "\nClock: ",listSeri_ram[j],"\nTDP: ",listSpeed_ram[j],
                "\nHarga: ",listHarga_ram[j])
        j=j+1
