from tkinter import *
import tkinter.ttk
from tkinter import messagebox
import timeit
from data_rakitan import *


start = timeit.default_timer()
# judul dan isi tabel
judul_kolom = ("MOTHERBOARD", "PROCESSOR", "RAM", "HDD", "VGA", "PSU", "HARGA")

class Tabel:
    def __init__(self, induk, judul):
        self.induk = induk
        
        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.aturKomponen()
        
    def aturKomponen(self):
        # buat frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)
    
        lbl = Label(mainFrame, text="Masukkan Budget",bd=0, relief=SUNKEN)
        lbl.pack(side=TOP, fill=X)
        global e1
        isi = StringVar(mainFrame, value=0)
        e1 = Entry(mainFrame,relief=SUNKEN,textvariable=isi)
        e1.pack(side=TOP, fill=Y)
        reqButton = Button(mainFrame, text='Enter', command=self.isiTabelRequest)
        reqButton.pack(side=TOP)
        button = Button(mainFrame, text='Show All Data', command=self.isiTabel)
        button.pack(side=TOP)
        # buat frame untuk tabel beserta scrollbar-nya
        fr_data = Frame(mainFrame, bd=10)
        fr_data.pack(fill=BOTH, expand=YES)
         
        # buat tabel dengan Treeview
        self.trvTabel = tkinter.ttk.Treeview(fr_data, columns=judul_kolom, 
                show='headings')
        
        # buat scrollbar
        sbVer = Scrollbar(fr_data, orient='vertical', 
                command=self.trvTabel.yview)
        sbHor = Scrollbar(fr_data, orient='horizontal', 
                command=self.trvTabel.xview)
        # pasang dengan layout manager pack()       
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)
        self.trvTabel.pack(side=LEFT, fill=BOTH)
        
        # buat statusbar
        lblStatus = Label(mainFrame, 
                text='© JOVEYO', bd=1, relief=SUNKEN)
        lblStatus.pack(side=BOTTOM, fill=X)
        
        # isi judul tabel
        for kolom in judul_kolom:
            self.trvTabel.heading(kolom, text=kolom)

    def isiTabelRequest(self):
        getData()
        data_pc = []
        maks = 0
        indexMaks = 0
        flag = False
        entry_budget = int(e1.get())
        if entry_budget == 0:
            messagebox.showerror("Error", "Budget Tidak Boleh 0")
        else:
            for i in self.trvTabel.get_children():
                self.trvTabel.delete(i)
            for i in range(len(indexMotherboard)):
                if i == 1 and hargaTotal[i] < entry_budget:
                    maks = hargaTotal[i]
                elif hargaTotal[i] > maks and hargaTotal[i] < entry_budget:
                    maks = hargaTotal[i]
                    indexMaks = i
                    flag = True
                elif i==len(indexMotherboard) and maks > entry_budget:
                    flag = False
            if flag == True:
                data_pc.append([listNama_motherboard[indexMotherboard[indexMaks]], listNama_processor[indexProcessor[indexMaks]],
                                 listNama_ram[indexRam[indexMaks]], listNama_hdd[indexHdd[indexMaks]],
                                 listNama_vga[indexVga[indexMaks]], listNama_psu[indexPsu[indexMaks]], hargaTotal[indexMaks]])
            elif flag == False:
                messagebox.showinfo("Info", "Budget Tidak Dapat Memenuhi Permintaan Rakitan")
            
            # isi data tabel
            for data in data_pc:
                self.trvTabel.insert('', 'end', values=data)
        stop = timeit.default_timer()
        print('Runtime: ', stop - start)

    def isiTabel(self):
        getData()
        data_pc = []
        for i in self.trvTabel.get_children():
            self.trvTabel.delete(i)
        for i in range(len(indexMotherboard)):
            data_pc.append([listNama_motherboard[indexMotherboard[i]], listNama_processor[indexProcessor[i]],
                             listNama_ram[indexRam[i]], listNama_hdd[indexHdd[i]],
                             listNama_vga[indexVga[i]], listNama_psu[indexPsu[i]], hargaTotal[i]])
        for data in data_pc:
            self.trvTabel.insert('', 'end', values=data)
            
        stop = timeit.default_timer()
        print('Runtime: ', stop - start)
        
    def Tutup(self, event = None):
        self.induk.destroy()
         
if __name__ == '__main__':
    root = Tk()
    app = Tabel(root, ":: Rakit PC V.1 ::")
     
    root.mainloop()
