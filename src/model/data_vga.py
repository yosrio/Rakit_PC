import pymysql

con = pymysql.connect(db="komponen_komputer", user="root", passwd="",
                  host="localhost", port=3306, autocommit=True)
nama_vga = con.cursor()
nama_vga.execute("SELECT nama_vga FROM vga;")
form_factor = con.cursor()
form_factor.execute("SELECT form_factor FROM vga;")
ukuran_memori = con.cursor()
ukuran_memori.execute("SELECT ukuran_memori FROM vga;")
tipe_memori = con.cursor()
tipe_memori.execute("SELECT tipe_memori FROM vga;")
tdp = con.cursor()
tdp.execute("SELECT tdp FROM vga;")
core_clock = con.cursor()
core_clock.execute("SELECT core_clock FROM vga;")
harga = con.cursor()
harga.execute("SELECT harga FROM vga;")

namaStr = nama_vga.fetchall()
form_factorStr = form_factor.fetchall()
ukuran_memoriint = ukuran_memori.fetchall()
tipe_memoristr = tipe_memori.fetchall()
tdpint = tdp.fetchall()
core_clockint = core_clock.fetchall()
hargaInt = harga.fetchall()

listNama_vga = []
listForm_factor_vga = []
listUkuranMemori_vga = []
listTipeMemori_vga = []
listTdp_vga = []
listCoreClock_vga = []
listHarga_vga = []

def strip_non_ascii(string):
    stripped = (c for c in string if ord(c) != 44 and ord(c) != 40 and
                ord(c) != 41 and ord(c) != 39)
    return ''.join(stripped)

def getDataVga():
    i=0
    while i<len(namaStr):
        str1 = str(namaStr[i])
        str2 = str(form_factorStr[i])
        str3 = str(ukuran_memoriint[i])
        str4 = str(tipe_memoristr[i])
        str5 = str(tdpint[i])
        str6 = str(core_clockint[i])
        str7 = str(hargaInt[i])
        
        listNama_vga.append(strip_non_ascii(str1))
        listForm_factor_vga.append(strip_non_ascii(str2))
        listUkuranMemori_vga.append(int(strip_non_ascii(str3)))
        listTipeMemori_vga.append(strip_non_ascii(str4))
        listTdp_vga.append(int(strip_non_ascii(str5)))
        listCoreClock_vga.append(int(strip_non_ascii(str6)))
        listHarga_vga.append(int(strip_non_ascii(str7)))
        i=i+1

def showVGA():
    getDataVga()
    j=0
    while j<len(listNama_vga):
        print("==============================")
        print("Merk: ",listNama_vga[j],"\nForm Factor: ",listForm_factor_vga[j],
                "\nUkuran Memori: ",listUkuranMemori_vga[j],"GB",
                "\nTipe Memori: ",listTipeMemori_vga[j],
                "\nTDP: ",listTdp_vga[j],"W","\nCore Clock: ",
                listCoreClock_vga[j],"\nHarga: ",listHarga_vga[j])
        j=j+1
