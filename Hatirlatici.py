from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

master = Tk()
master.title("Hatırlatıcı")
canvas = Canvas(master, height=450, width=750)
canvas.pack()

frame_ust = Frame(master, bg='#add8e6')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt_sol = Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.22, relwidth=0.23, relheight=0.5)

frame_alt_sag = Frame(master, bg='#add8e6')
frame_alt_sag.place(relx=0.35, rely=0.22, relwidth=0.55, relheight=0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6', font='verdana 12 bold', text='Hatırlatma Tipi:')
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set('\t')

hatirlatma_tipi_acilir_menu = OptionMenu(frame_ust, hatirlatma_tipi_opsiyon, "Doğum Günü", "Alışveriş", "Ödeme")
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarihi_secici = DateEntry(frame_ust, width=12, background='purple', foreground='black', borderwith=1)
hatirlatma_tarihi_secici._top_cal.overrideredirect(False)
hatirlatma_tarihi_secici.pack(padx=10, pady=10, side=RIGHT)

hatirlatma_tarihi_etiket = Label(frame_ust, bg='#add8e6', font='verdana 12 bold', text='Hatırlatma Tarihi:')
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=RIGHT)

Label(frame_alt_sol, bg='#add8e6', font='verdana 10 bold', text='Hatırlatma Yöntemi:').pack(padx=10, pady=10, anchor=NW)

var = IntVar()
R1 = Radiobutton(frame_alt_sol, bg='#add8e6', font='verdana 8', text='Sisteme Kaydet', variable=var, value=1)
R1.pack(padx=15, pady=5, anchor=NW)

R2 = Radiobutton(frame_alt_sol, bg='#add8e6', font='verdana 8', text='E-posta Gönder', variable=var, value=2)
R2.pack(padx=15, pady=5, anchor=NW)

var1 = IntVar()
C1 = Checkbutton(frame_alt_sol, bg='#add8e6', font='verdana 8', text='Bir ay önce', variable=var1, onvalue=1, offvalue=0)
C1.pack(padx=30, pady=5, anchor=NW)

var2 = IntVar()
C2 = Checkbutton(frame_alt_sol, bg='#add8e6', font='verdana 8', text='Bir hafta önce', variable=var2, onvalue=1, offvalue=0)
C2.pack(padx=30, pady=5, anchor=NW)

var3 = IntVar()
C3 = Checkbutton(frame_alt_sol, bg='#add8e6', font='verdana 8', text='Bir gün önce', variable=var3, onvalue=1, offvalue=0)
C3.pack(padx=30, pady=5, anchor=NW)

var4 = IntVar()
C4 = Checkbutton(frame_alt_sol, bg='#add8e6', font='verdana 8', text='Aynı Gün', variable=var4, onvalue=1, offvalue=0)
C4.pack(padx=30, pady=5, anchor=NW)

def gonder():
    son_mesaj = ""
    try:
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veriniz başarıyla kaydedilmiştir."
                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get() else 'Genel'
                tarih = hatirlatma_tarihi_secici.get()
                mesaj = metin_alani.get("1.0", "end")

                with open("hatırlatmalar.txt", "w") as dosya:
                    dosya.write("{} kategorisinde, {} tarihine ve '{}' notuyla hatırlatmanız var!".format(
                        tip,
                        tarih,
                        mesaj
                    ))
                    dosya.close()

            elif var.get() == 2:
                son_mesaj += "E-posta yoluyla hatırlatma size ulaşacaktır."
        
            messagebox.showinfo("Başarılı İşlem", son_mesaj)
        else:
            son_mesaj += "Gerekli alanların doldurulduğundan emin olun!"
            messagebox.showwarning("Yetersiz Bilgi", son_mesaj)
    except:
        son_mesaj += "İşlem başarısız oldu!"
        messagebox.showerror("Başarısız işlem", son_mesaj)
    finally:
        master.destroy()
    return

Label(frame_alt_sag, bg='#add8e6', font='verdana 10 bold', text='Hatırlatma Mesajı:').pack(padx=10, pady=10, anchor=NW)

metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_configure('style', foreground='#bfbfbf', font='verdana 10 bold')
metin_alani.pack()

karsilama_metni = 'Mesajını buraya gir...'
metin_alani.insert(END, karsilama_metni, 'style')

gonder_butonu = Button(frame_alt_sag, text='Gönder', command=gonder)
gonder_butonu.pack(anchor=S, pady=5)

master.mainloop()