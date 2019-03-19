import pymysql

con = pymysql.connect(db="komponen_komputer", user="root", passwd="",
                  host="localhost", port=3306, autocommit=True)
nama_motherboard = con.cursor()
nama_motherboard.execute("SELECT nama_motherboard FROM motherboard;")
chipset = con.cursor()
chipset.execute("SELECT chipset FROM motherboard;")
socket = con.cursor()
socket.execute("SELECT socket FROM motherboard;")
tipe_memori = con.cursor()
tipe_memori.execute("SELECT tipe_memori FROM motherboard;")
slot_memori = con.cursor()
slot_memori.execute("SELECT slot_memori FROM motherboard;")
maksimal_memori = con.cursor()
maksimal_memori.execute("SELECT maksimal_memori FROM motherboard;")
interface_storage = con.cursor()
interface_storage.execute("SELECT interface_storage FROM motherboard;")
form_factor = con.cursor()
form_factor.execute("SELECT form_factor FROM motherboard;")
harga = con.cursor()
harga.execute("SELECT harga FROM motherboard;")

namaStr = nama_motherboard.fetchall()
chipsetStr = chipset.fetchall()
socketStr = socket.fetchall()
tipe_memoriStr = tipe_memori.fetchall()
slot_memoriStr = slot_memori.fetchall()
maksimal_memoriInt = maksimal_memori.fetchall()
interface_storageStr = interface_storage.fetchall()
form_factorStr = form_factor.fetchall()
hargaInt = harga.fetchall()

listNama_motherboard = []
listChipset_motherboard = []
listSocket_motherboard = []
listTipe_memori_motherboard = []
listSlot_memori_motherboard = []
listMaksimal_memori_motherboard = []
listInterface_storage_motherboard = []
listForm_factor_motherboard = []
listHarga_motherboard = []

def strip_non_ascii(string):
    stripped = (c for c in string if ord(c) != 44 and ord(c) != 40 and
                ord(c) != 41 and ord(c) != 39)
    return ''.join(stripped)

def getDataMotherboard():
    i=0
    while i<len(namaStr):
        str1 = str(namaStr[i])
        str2 = str(chipsetStr[i])
        str3 = str(socketStr[i])
        str4 = str(tipe_memoriStr[i])
        str5 = str(slot_memoriStr[i])
        str6 = str(maksimal_memoriInt[i])
        str7 = str(interface_storageStr[i])
        str8 = str(form_factorStr[i])
        str9 = str(hargaInt[i])
        
        listNama_motherboard.append(strip_non_ascii(str1))
        listChipset_motherboard.append(strip_non_ascii(str2))
        listSocket_motherboard.append(strip_non_ascii(str3))
        listTipe_memori_motherboard.append(strip_non_ascii(str4))
        listSlot_memori_motherboard.append(strip_non_ascii(str5))
        listMaksimal_memori_motherboard.append(int(strip_non_ascii(str6)))
        listInterface_storage_motherboard.append(strip_non_ascii(str7))
        listForm_factor_motherboard.append(strip_non_ascii(str8))
        listHarga_motherboard.append(int(strip_non_ascii(str9)))
        i=i+1

def showMotherboard():
    getDataMotherboard()
    j=0
    while j<len(listNama_motherboard):
        print("==============================")
        print("Nama: ",listNama_motherboard[j],"\nChipset: ",listChipset_motherboard[j],"\nSocket: ",
                listSocket_motherboard[j],"\nSupport Memory: ",listTipe_memori_motherboard[j],
                "\nMaksimal Slot Memory: ",listSlot_memori_motherboard[j],"\nMaksimal Memory: ",listMaksimal_memori_motherboard[j]," GB",
                "\nStorage: ",listInterface_storage_motherboard[j],"\nForm Factor: ",listForm_factor_motherboard[j],
                "\nHarga: ",listHarga_motherboard[j])
        j=j+1
