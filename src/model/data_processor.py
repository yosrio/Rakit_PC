import pymysql

con = pymysql.connect(db="komponen_komputer", user="root", passwd="",
                  host="localhost", port=3306, autocommit=True)
nama_processor = con.cursor()
nama_processor.execute("SELECT nama_processor FROM processor;")
model_number = con.cursor()
model_number.execute("SELECT model_number FROM processor;")
socket = con.cursor()
socket.execute("SELECT socket FROM processor;")
core = con.cursor()
core.execute("SELECT core FROM processor;")
clock = con.cursor()
clock.execute("SELECT clock FROM processor;")
tdp = con.cursor()
tdp.execute("SELECT tdp FROM processor;")
harga = con.cursor()
harga.execute("SELECT harga FROM processor;")

namaStr = nama_processor.fetchall()
model_numberStr = model_number.fetchall()
socketStr = socket.fetchall()
coreStr = core.fetchall()
clockInt = clock.fetchall()
tdpInt = tdp.fetchall()
hargaInt = harga.fetchall()

listNama_processor = []
listModel_number_processor = []
listSocket_processor = []
listCore_processor = []
listClock_processor = []
listTdp_processor = []
listHarga_processor = []

def strip_non_ascii(string):
    stripped = (c for c in string if ord(c) != 44 and ord(c) != 40 and
                ord(c) != 41 and ord(c) != 39)
    return ''.join(stripped)

def getDataProcessor():
    i=0
    while i<len(namaStr):
        str1 = str(namaStr[i])
        str2 = str(model_numberStr[i])
        str3 = str(socketStr[i])
        str4 = str(coreStr[i])
        str5 = str(clockInt[i])
        str6 = str(tdpInt[i])
        str9 = str(hargaInt[i])
        
        listNama_processor.append(strip_non_ascii(str1))
        listModel_number_processor.append(strip_non_ascii(str2))
        listSocket_processor.append(strip_non_ascii(str3))
        listCore_processor.append(strip_non_ascii(str4))
        listClock_processor.append(int(strip_non_ascii(str5)))
        listTdp_processor.append(int(strip_non_ascii(str6)))
        listHarga_processor.append(int(strip_non_ascii(str9)))
        i=i+1

def showProcessor():
    getDataProcessor()
    j=0
    while j<len(listNama_processor):
        print("==============================")
        print("Nama: ",listNama_processor[j],"\nModel Number: ",listModel_number_processor[j],"\nSocket: ",
                listSocket_processor[j],"\nCore: ",listCore_processor[j],
                "\nClock: ",listClock_processor[j],"\nTDP: ",listTdp_processor[j],
                "\nHarga: ",listHarga_processor[j])
        j=j+1
