from data_vga import *
from data_hdd import *
from data_motherboard import *
from data_processor import *
from data_psu import *
from data_ram import *

getDataMotherboard()
getDataProcessor()
getDataRam()
getDataHdd()
getDataPsu()
getDataVga()

hargaTotal = []
indexMotherboard = []
indexProcessor = []
indexRam = []
indexHdd = []
indexVga = []
indexPsu = []

def getData():
    global hargaTotal
    global indexMotherboard
    global indexProcessor
    global indexRam
    global hargaTotal
    global indexHdd
    global indexVga
    global indexPsu
    for i in range(len(listSocket_motherboard)):
        for j in range(len(listSocket_processor)):
            for k in range(len(listNama_ram)):
                for l in range(len(listNama_hdd)):
                    for m in range(len(listNama_vga)):
                        for n in range(len(listNama_psu)):
                            if listSocket_motherboard[i] == listSocket_processor[j]:
                                if listTipe_memori_motherboard[i] == listTipe_ram[k]:
                                    if listInterface_storage_motherboard[i] == listInterface_hdd[l]:
                                        if listForm_factor_motherboard[i] == listForm_factor_vga[m]:
                                            if listForm_factor_motherboard[i] == listForm_factor_psu[n]:
                                                indexMotherboard.append(i)
                                                indexProcessor.append(j)
                                                indexRam.append(k)
                                                indexHdd.append(l)
                                                indexVga.append(m)
                                                indexPsu.append(n)
                                                harga = listHarga_motherboard[i] + listHarga_processor[j] + listHarga_ram[k]
                                                harga = harga + listHarga_hdd[l] + listHarga_vga[m] + listHarga_psu[n]
                                                hargaTotal.append(harga)

