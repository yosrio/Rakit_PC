import pymysql

con = pymysql.connect(db="komponen_komputer", user="root", passwd="",
                  host="localhost", port=3306, autocommit=True)
nama_hdd = con.cursor()
nama_hdd.execute("SELECT nama_hdd FROM harddisk;")
interface = con.cursor()
interface.execute("SELECT interface FROM harddisk;")
kapasitas = con.cursor()
kapasitas.execute("SELECT kapasitas FROM harddisk;")
cache = con.cursor()
cache.execute("SELECT cache FROM harddisk;")
speed = con.cursor()
speed.execute("SELECT speed FROM harddisk;")
form_factor = con.cursor()
form_factor.execute("SELECT form_factor FROM harddisk;")
harga = con.cursor()
harga.execute("SELECT harga FROM harddisk;")

namaStr = nama_hdd.fetchall()
interfaceStr = interface.fetchall()
kapasitasInt = kapasitas.fetchall()
cacheInt = cache.fetchall()
speedInt = speed.fetchall()
form_factorStr = form_factor.fetchall()
hargaInt = harga.fetchall()

listNama_hdd = []
listInterface_hdd = []
listKapasitas_hdd = []
listCache_hdd = []
listSpeed_hdd = []
listForm_factor_hdd = []
listHarga_hdd = []

def strip_non_ascii(string):
    stripped = (c for c in string if ord(c) != 44 and ord(c) != 40 and
                ord(c) != 41 and ord(c) != 39)
    return ''.join(stripped)

def getDataHdd():
    i=0
    while i<len(namaStr):
        str1 = str(namaStr[i])
        str2 = str(interfaceStr[i])
        str3 = str(kapasitasInt[i])
        str4 = str(cacheInt[i])
        str5 = str(speedInt[i])
        str6 = str(form_factorStr[i])
        str7 = str(hargaInt[i])
        
        listNama_hdd.append(strip_non_ascii(str1))
        listInterface_hdd.append(strip_non_ascii(str2))
        listKapasitas_hdd.append(int(strip_non_ascii(str3)))
        listCache_hdd.append(int(strip_non_ascii(str4)))
        listSpeed_hdd.append(int(strip_non_ascii(str5)))
        listForm_factor_hdd.append(strip_non_ascii(str6))
        listHarga_hdd.append(int(strip_non_ascii(str7)))
        i=i+1

def showHdd():
    getDataHdd()
    j=0
    while j<len(listNama_hdd):
        print("==============================")
        print("Nama: ",listNama_hdd[j],"\nKapasitas: ",listKapasitas_hdd[j],"\nInterface: ",listInterface_hdd[j],
                "\nCache: ",listCache_hdd[j],"\nSpeed: ",listSpeed_hdd[j],
                "\nForm Factor: ",listForm_factor_hdd[j],"\nHarga: ",listHarga_hdd[j])
        j=j+1
