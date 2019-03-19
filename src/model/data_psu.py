import pymysql

con = pymysql.connect(db="komponen_komputer", user="root", passwd="",
                  host="localhost", port=3306, autocommit=True)
nama_psu = con.cursor()
nama_psu.execute("SELECT nama_psu FROM power_supply;")
modular_cable_management = con.cursor()
modular_cable_management.execute("SELECT modular_cable_management FROM power_supply;")
sleeved_cable = con.cursor()
sleeved_cable.execute("SELECT sleeved_cable FROM power_supply;")
form_factor = con.cursor()
form_factor.execute("SELECT form_factor FROM power_supply;")
efficiency = con.cursor()
efficiency.execute("SELECT efficiency FROM power_supply;")
power_supply = con.cursor()
power_supply.execute("SELECT power_supply FROM power_supply;")
harga = con.cursor()
harga.execute("SELECT harga FROM power_supply;")

namaStr = nama_psu.fetchall()
mcmStr = modular_cable_management.fetchall()
sleeved_cableStr = sleeved_cable.fetchall()
form_factorStr = form_factor.fetchall()
efficiencyStr = efficiency.fetchall()
power_supplyInt = power_supply.fetchall()
hargaInt = harga.fetchall()

listNama_psu = []
listMcm_psu = []
listSleveed_cable_psu = []
listForm_factor_psu = []
listEfficiency_psu = []
listPower_supply_psu = []
listHarga_psu = []

def strip_non_ascii(string):
    stripped = (c for c in string if ord(c) != 44 and ord(c) != 40 and
                ord(c) != 41 and ord(c) != 39)
    return ''.join(stripped)

def getDataPsu():
    i=0
    while i<len(namaStr):
        str1 = str(namaStr[i])
        str2 = str(mcmStr[i])
        str3 = str(sleeved_cableStr[i])
        str4 = str(form_factorStr[i])
        str5 = str(efficiencyStr[i])
        str6 = str(power_supplyInt[i])
        str7 = str(hargaInt[i])
        
        listNama_psu.append(strip_non_ascii(str1))
        listMcm_psu.append(strip_non_ascii(str2))
        listSleveed_cable_psu.append(strip_non_ascii(str3))
        listForm_factor_psu.append(strip_non_ascii(str4))
        listEfficiency_psu.append(strip_non_ascii(str5))
        listPower_supply_psu.append(int(strip_non_ascii(str6)))
        listHarga_psu.append(int(strip_non_ascii(str7)))
        i=i+1

def showPsu():
    getDataPsu()
    j=0
    while j<len(listNama_psu):
        print("==============================")
        print("Nama: ",listNama_psu[j],"\nModular Cable Management: ",listMcm_psu[j],"\nSleveed Cable: ",
                listSleveed_cable_psu[j],"\nForm Factor: ",listForm_factor_psu[j],"\nEfficiency: ",listEfficiency_psu[j],
                "\nPower: ",listPower_supply_psu[j],"\nHarga: ",listHarga_psu[j])
        j=j+1
