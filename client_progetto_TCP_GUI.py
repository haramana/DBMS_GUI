#HARMAN SINGH
'''
problemi : il contatore non è un problema ma la gestione del server pk se schiaccio delete invio al server D e entro nella funzione db_delete() 
poi se faccio back e schiaccio insert invio I ma sono ancora nella funzione db_delete() usa qualche flag!!!

'''


import socket
import customtkinter as tk
import tkinter as t
from PIL import Image
import os                   
import time

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")
root = tk.CTk()
root.geometry("800x500")
root.title("DATABASE EINAUDI")

flag_prima_VOLTA_dip_o_zone= True 
flag_prima_VOLTA_read= True
flag_prima_VOLTA_read_stampaDIP=True
flag_prima_VOLTA_read_stampaZONE=True
flag_prima_VOLTA_insert_dip=True
flag_prima_VOLTA_insert_zone=True
flag_prima_VOLTA_update_zone=True
flag_prima_VOLTA_update_dip=True

i = 0
global user_entry
global password_entry
global j


j=0
finestra_attuale = None
bottone_attuale= None


frame_enter = tk.CTkFrame(master=root)
frame_login = tk.CTkFrame(master=root)
frame_admin = tk.CTkFrame(master=root)
frame_dip_o_zone= tk.CTkFrame(master=root)
frame_dip_o_zone_del= tk.CTkFrame(master=root)
frame_read = tk.CTkFrame(master=root)
frame_insert_dip = tk.CTkFrame(master=root)
frame_insert_zone= tk.CTkFrame(master=root)
frame_delete = tk.CTkFrame(master=root)
frame_eliminazione_dip=tk.CTkFrame(master=root)
frame_eliminazione_zone=tk.CTkFrame(master=root)
frame_stampa_dip=tk.CTkFrame(master=root)
frame_update=tk.CTkFrame(master=root) # <-- dipendenti
frame_update_zone=tk.CTkFrame(master=root)
frame_dip_zone_update=tk.CTkFrame(master=root)
frame_stampa_zone=tk.CTkFrame(master=root)

def quit():
    root.destroy()


def back():
    global i
    global finestra_attuale
    global bottone_attuale
    #inizio
    
    print(finestra_attuale)
    print(bottone_attuale)
    finestra_attuale.pack_forget()
    bottone_attuale.pack_forget()
    i+=1
    admin()
def back_upd():
    global i
    global finestra_attuale
    print(finestra_attuale)
    finestra_attuale.pack_forget()
    i+=1
    admin()

def back_read():
    global i
    global finestra_attuale
    global bottone_attuale
    finestra_attuale.destroy()
    bottone_attuale.destroy()
    i+=1
    admin()

def update():
    global finestra_attuale
    global bottone_attuale
    finestra_attuale=frame_update
    bottone_attuale= button_back_update
    frame_admin.pack_forget()
    frame_update.pack()
    button_back_update.pack()

###################################################################################################################
def deleted_zone(frame):
    
    id_zona=frame.get()
    s.send(id_zona.encode())
    print("ELIMINATO")
    back()



def eliminazione_zone():
    global i
    if i==0:
        global finestra_attuale
        global bottone_attuale
        s.send("zone_di_lavoro".encode())
        finestra_attuale=frame_eliminazione_zone
        
        frame_dip_o_zone_del.pack_forget()
        frame_eliminazione_zone.pack()

        label=tk.CTkLabel(master=frame_eliminazione_zone, text="INSERISCI ID DELLA ZONA", font=("Roboto", 20))
        label.pack()

        entrata=tk.CTkEntry(master=frame_eliminazione_zone, placeholder_text="ID")
        entrata.pack(pady=100, padx=100)

        bottone_invio=tk.CTkButton(master=frame_eliminazione_zone, command=lambda: deleted_zone(entrata), text="INVIO")
        bottone_invio.pack()
    else:
        frame_dip_o_zone_del.pack_forget()
        frame_eliminazione_zone.pack()



def deleted_dip(frame) :
    
    
    id=frame.get()
    s.send(id.encode())
    
    back()


def eliminazione_dip():
    global i
    if i==0:
        global finestra_attuale
        global bottone_attuale
        finestra_attuale=frame_eliminazione_dip

        frame_dip_o_zone_del.pack_forget()
        s.send("dipendenti".encode())
        frame_eliminazione_dip.pack()
        label=tk.CTkLabel(master=frame_eliminazione_dip, text="INSERISCI ID DEL DIPENDENTE DA ELIMINARE", font=("Roboto", 28))
        label.pack()
        inserimento=tk.CTkEntry(master=frame_eliminazione_dip, placeholder_text="id")
        inserimento.pack(pady=100, padx=100)

        bottone_invio=tk.CTkButton(master=frame_eliminazione_dip, command= lambda: deleted_dip(inserimento), text="INVIA")
        bottone_invio.pack()
    else:
        frame_dip_o_zone_del.pack_forget()
        frame_eliminazione_dip.pack()

# PROBLEMI QUI GIU !!!

def dip_o_zone_delete():
    s.send("D".encode())
    global i
    j=0
    global finestra_attuale
    global bottone_attuale
    if i >= 0:
        #global finestra_attuale
        #global bottone_attuale
        finestra_attuale=frame_dip_o_zone_del
        bottone_attuale=button_back_dip_o_zone_del
        frame_admin.pack_forget()
        frame_dip_o_zone_del.pack()
        titolo_dip_zone=tk.CTkLabel(master=frame_dip_o_zone_del, text="SCEGLI QUALE TABELLA", font=("Roboto", 28))
        titolo_dip_zone.pack()
        dip_bottone=tk.CTkButton(master=frame_dip_o_zone_del, text="DIPENDENTI", command=eliminazione_dip, fg_color="Blue")
        dip_bottone.pack(side="right")
        zone_bottone=tk.CTkButton(master=frame_dip_o_zone_del, text="ZONE DI LAVORO",command=eliminazione_zone,  fg_color="Red")
        zone_bottone.pack(side="left")
        #button_back_dip_o_zone_del.pack()
        j+=1
        i=0


    elif j>1:
        print("sono zzala")
        finestra_attuale.pack_forget()
        bottone_attuale.pack_forget()
        frame_admin.pack_forget()
        frame_dip_o_zone.pack()
        #button_back_dip_o_zone_del.pack()

######################################################################################################################
def azione_upd_zone(update_id_zona, update_nome_zona, update_num_clienti, update_id_dip, update_reparto):
    id_zona=update_id_zona.get()
    id_zona=id_zona.encode()
    nome_zona=update_nome_zona.get()
    nome_zona=nome_zona.encode()
    num_clienti=update_num_clienti.get()
    num_clienti=num_clienti.encode()
    id_dip=update_id_dip.get()
    id_dip=id_dip.encode()
    reparto=update_reparto.get()
    reparto=reparto.encode()

    s.send(id_zona)
    s.send(nome_zona)
    s.send(num_clienti)
    s.send(id_dip)
    s.send(data)
    s.send(reparto)
    time.sleep(2)

    print("updatato")
    back_upd()




def update_zone(): 
    s.send("zone_di_lavoro".encode())
    global i
    global finestra_attuale
    global bottone_attuale
    global flag_prima_VOLTA_update_zone
    if i==0 and flag_prima_VOLTA_update_zone:
        finestra_attuale=frame_update_zone
        bottone_attuale=None
        frame_dip_zone_update.pack_forget()
        frame_update_zone.pack()

        titolo_insert_zone=tk.CTkLabel(master=frame_update_zone, text="INSERISCI I DATI", font=("Roboto", 24), text_color="blue")
        titolo_insert_zone.pack(pady=5, padx=5)
        update_id_zona=tk.CTkEntry(master=frame_update_zone, placeholder_text="id del dip da updatare")
        update_id_zona.pack(pady=5, padx=5)
        update_nome_zona=tk.CTkEntry(master=frame_update_zone, placeholder_text="nome della zona")
        update_nome_zona.pack(pady=5, padx=5)
        update_num_clienti=tk.CTkEntry(master=frame_update_zone, placeholder_text="numero clienti")
        update_num_clienti.pack(pady=5, padx=5)
        update_id_dip=tk.CTkEntry(master=frame_update_zone, placeholder_text="id del dipendente")
        update_id_dip.pack(pady=5, padx=5)
        update_reparto=tk.CTkEntry(master=frame_update_zone, placeholder_text="reparto")
        update_reparto.pack(pady=5, padx=5)
        bottone_press4=tk.CTkButton(master=frame_update_zone, command=lambda: azione_upd_zone(update_id_zona, update_nome_zona, update_num_clienti, update_id_dip, update_reparto,), text="INVIA ZONE")
        bottone_press4.pack(pady=5, padx=5)
        if flag_prima_VOLTA_update_zone:
            print("La prima volta ALPHA")
            flag_prima_VOLTA_update_zone = False
    else:
        frame_dip_zone_update.pack_forget()
        frame_update_zone.pack()






def azione_upd_dip(update_id, update_nome, update_cognome, update_pos, update_data, update_eta, update_ind): 

    id=update_id.get()
    id=id.encode()
    nome=update_nome.get()
    nome=nome.encode()
    cognome=update_cognome.get()
    cognome=cognome.encode()
    pos=update_pos.get()
    pos=pos.encode()
    data=update_data.get()
    data=data.encode()
    eta=update_eta.get()
    eta=eta.encode()
    ind=update_ind.get()
    ind=ind.encode()

    s.send(id)
    s.send(nome)
    s.send(cognome)
    s.send(pos)
    s.send(data)
    s.send(eta)
    s.send(ind)

    print("updatato")
    back_upd()



def dip_update(): 
    s.send("dipendenti".encode())
    global i
    global finestra_attuale
    global bottone_attuale
    global flag_prima_VOLTA_update_dip

    if i==0 and flag_prima_VOLTA_update_dip: 
        finestra_attuale=frame_update
        bottone_attuale=None
        frame_dip_zone_update.pack_forget()
        frame_update.pack()
        titolo_insert_dip=tk.CTkLabel(master=frame_update, text="INSERISCI I DATI", font=("Roboto", 24), text_color="blue")
        titolo_insert_dip.pack(pady=5, padx=5)
        update_id=tk.CTkEntry(master=frame_update, placeholder_text="id del dip da updatare")
        update_id.pack(pady=5, padx=5)
        update_nome=tk.CTkEntry(master=frame_update, placeholder_text="nome")
        update_nome.pack(pady=5, padx=5)
        update_cognome=tk.CTkEntry(master=frame_update, placeholder_text="cognome")
        update_cognome.pack(pady=5, padx=5)
        update_pos=tk.CTkEntry(master=frame_update, placeholder_text="posizione lavorativa: ")
        update_pos.pack(pady=5, padx=5)
        update_data=tk.CTkEntry(master=frame_update, placeholder_text="data: AA-MM-GG")
        update_data.pack(pady=5, padx=5)
        update_eta=tk.CTkEntry(master=frame_update, placeholder_text="anno")
        update_eta.pack(pady=5, padx=5)
        update_ind=tk.CTkEntry(master=frame_update, placeholder_text="indirizzo")
        update_ind.pack(pady=5, padx=5)
        bottone_press3=tk.CTkButton(master=frame_update, command=lambda: azione_upd_dip(update_id, update_nome, update_cognome, update_pos, update_data, update_eta, update_ind), text="INVIA")
        bottone_press3.pack(pady=5, padx=5)
        if flag_prima_VOLTA_update_dip:
            print("La prima volta ALPHA")
            flag_prima_VOLTA_update_dip = False
    else: 
        frame_dip_zone_update.pack_forget()
        frame_update.pack()




        



def dip_o_zone_update():

    s.send("U".encode())
    global i
    global finestra_attuale
    global bottone_attuale

    if i >=0: 
        finestra_attuale=frame_dip_zone_update
        frame_admin.pack_forget()
        frame_dip_zone_update.pack()
        titolo_dip_zone=tk.CTkLabel(master=frame_dip_zone_update, text="SCEGLI QUALE TABELLA", font=("Roboto", 28))
        titolo_dip_zone.pack()
        dip_bottone2=tk.CTkButton(master=frame_dip_zone_update, text="DIPENDENTI", command=dip_update, fg_color="Blue")
        dip_bottone2.pack(pady=5, padx=5)
        zone_bottone2=tk.CTkButton(master=frame_dip_zone_update, text="ZONE DI LAVORO",command=update_zone,  fg_color="Red")
        zone_bottone2.pack(pady=5, padx=5)
    else: 
        frame_admin.pack_forget()
        frame_dip_zone_update.pack()







######################################################################################################################################################################
def invia_zone(insert_nome_zona, insert_num_clienti, insert_id_dip, insert_reparto): 
    
    nome_zona=insert_nome_zona.get()
    nome_zona=nome_zona.encode()
    num_clienti=insert_num_clienti.get()
    num_clienti=num_clienti.encode()
    id_dip=insert_id_dip.get()
    id_dip=id_dip.encode()
    reparto=insert_reparto.get()
    reparto=reparto.encode()

    s.send(nome_zona)
    s.send(num_clienti)
    s.send(id_dip)
    s.send(reparto)

    print("inviato")
    back()





def insert_zone():
    global i
    s.send("zone_di_lavoro".encode())
    global finestra_attuale
    global bottone_attuale
    global flag_prima_VOLTA_insert_zone
    if i == 0 and flag_prima_VOLTA_insert_zone: 
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        finestra_attuale=frame_insert_zone
        bottone_attuale=button_back_insert_zone
        frame_dip_o_zone.pack_forget()
        frame_insert_zone.pack()
        titolo_insert_zone=tk.CTkLabel(master=frame_insert_zone, text="INSERISCI I DATI", font=("Roboto", 24), text_color="blue")
        titolo_insert_zone.pack()

        insert_nome_zona=tk.CTkEntry(master=frame_insert_zone, placeholder_text="nome della zona")
        insert_nome_zona.pack(pady=5, padx=5)
        insert_num_clienti=tk.CTkEntry(master=frame_insert_zone, placeholder_text="numero clienti")
        insert_num_clienti.pack(pady=5, padx=5)
        insert_id_dip=tk.CTkEntry(master=frame_insert_zone, placeholder_text="id del dipendente")
        insert_id_dip.pack(pady=5, padx=5)
        insert_reparto=tk.CTkEntry(master=frame_insert_zone, placeholder_text="reparto")
        insert_reparto.pack(pady=5, padx=5)

        button_back_insert_zone.pack()
        bottone_press2=tk.CTkButton(master=frame_insert_zone, command=lambda: invia_zone(insert_nome_zona, insert_num_clienti, insert_id_dip, insert_reparto), text="INVIA")
        bottone_press2.pack()
        if flag_prima_VOLTA_insert_zone:
            print("La prima volta BETA")
            flag_prima_VOLTA_insert_zone = False

    elif flag_prima_VOLTA_insert_zone:
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        finestra_attuale=frame_insert_zone
        bottone_attuale=button_back_insert_zone
        frame_dip_o_zone.pack_forget()
        frame_insert_zone.pack()
        titolo_insert_zone=tk.CTkLabel(master=frame_insert_zone, text="INSERISCI I DATI", font=("Roboto", 24), text_color="blue")
        titolo_insert_zone.pack()

        insert_nome_zona=tk.CTkEntry(master=frame_insert_zone, placeholder_text="nome della zona")
        insert_nome_zona.pack(pady=5, padx=5)
        insert_num_clienti=tk.CTkEntry(master=frame_insert_zone, placeholder_text="numero clienti")
        insert_num_clienti.pack(pady=5, padx=5)
        insert_id_dip=tk.CTkEntry(master=frame_insert_zone, placeholder_text="id del dipendente")
        insert_id_dip.pack(pady=5, padx=5)
        insert_reparto=tk.CTkEntry(master=frame_insert_zone, placeholder_text="reparto")
        insert_reparto.pack(pady=5, padx=5)

        button_back_insert_zone.pack(pady=5, padx=5)
        bottone_press2=tk.CTkButton(master=frame_insert_zone, command=lambda: invia_zone(insert_nome_zona, insert_num_clienti, insert_id_dip, insert_reparto), text="INVIA")
        bottone_press2.pack()
        if flag_prima_VOLTA_insert_zone:
            print("La prima volta BETA")
            flag_prima_VOLTA_insert_zone = False

    else:
        finestra_attuale=frame_insert_dip
        bottone_attuale=button_back_insert_dip
        frame_dip_o_zone.pack_forget()
        frame_insert_zone.pack()
        button_back_insert_zone.pack()


def invia_dip(insert_nome, insert_cognome, insert_pos, insert_data, insert_eta, insert_ind):
    nome=insert_nome.get()
    nome=nome.encode()
    cognome=insert_cognome.get()
    cognome=cognome.encode()
    pos=insert_pos.get()
    pos=pos.encode()
    data=insert_data.get()
    data=data.encode()
    eta=insert_eta.get()
    eta=eta.encode()
    ind=insert_ind.get()
    ind=ind.encode()
    '''
    
    gli sleep servono per sincronizzare gli invii dei dati perchè senza gli sleep i dati vengono ricevuti in unico 
    recv() e il server aspetta l'arrivo dei altri dati.
    
    '''

    print(nome, cognome, pos, data, eta, ind)
    print("inviato")
    s.send(nome)
    time.sleep(0.5)
    s.send(cognome)
    time.sleep(0.5)
    s.send(pos)
    time.sleep(0.5)
    s.send(data)
    time.sleep(0.5)
    s.send(eta)
    time.sleep(0.5)
    s.send(ind)
    print("inviato 2")
    back()

def insert_dip():
    global i
    global flag_prima_VOLTA_insert_dip
    s.send("dipendenti".encode())
    global finestra_attuale
    global bottone_attuale
    if i == 0 and flag_prima_VOLTA_insert_dip:
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        finestra_attuale=frame_insert_dip
        bottone_attuale=button_back_insert_dip
        frame_dip_o_zone.pack_forget()
        frame_insert_dip.pack()
            
        titolo_insert_dip=tk.CTkLabel(master=frame_insert_dip, text="INSERISCI I DATI", font=("Roboto", 24), text_color="blue")
        titolo_insert_dip.pack(pady=5, padx=5)
        insert_nome=tk.CTkEntry(master=frame_insert_dip, placeholder_text="nome")
        insert_nome.pack(pady=5, padx=5)
        insert_cognome=tk.CTkEntry(master=frame_insert_dip, placeholder_text="cognome")
        insert_cognome.pack(pady=5, padx=5)
        insert_pos=tk.CTkEntry(master=frame_insert_dip, placeholder_text="posizione lavorativa: ")
        insert_pos.pack(pady=5, padx=5)
        insert_data=tk.CTkEntry(master=frame_insert_dip, placeholder_text="data: AA-MM-GG")
        insert_data.pack(pady=5, padx=5)
        insert_eta=tk.CTkEntry(master=frame_insert_dip, placeholder_text="anno")
        insert_eta.pack(pady=5, padx=5)
        insert_ind=tk.CTkEntry(master=frame_insert_dip, placeholder_text="indirizzo")
        insert_ind.pack(pady=5, padx=5)

        button_back_insert_dip.pack()

        buttone_press=tk.CTkButton(master=frame_insert_dip, command=lambda: invia_dip(insert_nome, insert_cognome, insert_pos, insert_data, insert_eta, insert_ind), text="INVIA", ) # lambda serve per passare piu valori a una funzione
        buttone_press.pack()
        if flag_prima_VOLTA_insert_dip:
            print("La prima volta BETA")
            flag_prima_VOLTA_insert_dip = False
    
    elif flag_prima_VOLTA_insert_dip: 
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        finestra_attuale=frame_insert_dip
        bottone_attuale=button_back_insert_dip
        frame_dip_o_zone.pack_forget()
        frame_insert_dip.pack()
            
        titolo_insert_dip=tk.CTkLabel(master=frame_insert_dip, text="INSERISCI I DATI", font=("Roboto", 24), text_color="blue")
        titolo_insert_dip.pack(pady=5, padx=5)
        insert_nome=tk.CTkEntry(master=frame_insert_dip, placeholder_text="nome")
        insert_nome.pack(pady=5, padx=5)
        insert_cognome=tk.CTkEntry(master=frame_insert_dip, placeholder_text="cognome")
        insert_cognome.pack(pady=5, padx=5)
        insert_pos=tk.CTkEntry(master=frame_insert_dip, placeholder_text="posizione lavorativa: ")
        insert_pos.pack(pady=5, padx=5)
        insert_data=tk.CTkEntry(master=frame_insert_dip, placeholder_text="data: AA-MM-GG")
        insert_data.pack(pady=5, padx=5)
        insert_eta=tk.CTkEntry(master=frame_insert_dip, placeholder_text="anno")
        insert_eta.pack(pady=5, padx=5)
        insert_ind=tk.CTkEntry(master=frame_insert_dip, placeholder_text="indirizzo")
        insert_ind.pack(pady=5, padx=5)

        button_back_insert_dip.pack()

        buttone_press=tk.CTkButton(master=frame_insert_dip, command=lambda: invia_dip(insert_nome, insert_cognome, insert_pos, insert_data, insert_eta, insert_ind), text="INVIA", ) # lambda serve per passare piu valori a una funzione
        buttone_press.pack(pady=5, padx=5)
        if flag_prima_VOLTA_insert_dip:
            print("La prima volta BETA")
            flag_prima_VOLTA_insert_dip = False
        

    else:
        finestra_attuale=frame_insert_dip
        bottone_attuale=button_back_insert_dip
        frame_dip_o_zone.pack_forget()
        frame_insert_dip.pack()
        button_back_insert_dip.pack()



def dip_o_zone():

    s.send("I".encode())
    global i
    global j
    global flag_prima_VOLTA_dip_o_zone
    global finestra_attuale
    global bottone_attuale
        

    
    if i == 0:
        print("paolo")
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        print("paolo 2")
        print(f"sono in dip_o_zone {i}")
        global finestra_attuale
        global bottone_attuale
        finestra_attuale=frame_dip_o_zone
        bottone_attuale=button_back_dip_o_zone
        frame_admin.pack_forget()
        frame_dip_o_zone.pack()
        titolo_dip_zone=tk.CTkLabel(master=frame_dip_o_zone, text="SCEGLI QUALE TABELLA", font=("Roboto", 28))            
        titolo_dip_zone.pack()
        dip_bottone=tk.CTkButton(master=frame_dip_o_zone, text="DIPENDENTI", command=insert_dip, fg_color="Blue")
        dip_bottone.pack(side="right")
        zone_bottone=tk.CTkButton(master=frame_dip_o_zone, text="ZONE DI LAVORO",command=insert_zone,  fg_color="Red")            
        zone_bottone.pack(side="left")
    
         
        if flag_prima_VOLTA_dip_o_zone:
            print("La prima volta OMEGA")
            flag_prima_VOLTA_dip_o_zone = False

    elif flag_prima_VOLTA_dip_o_zone == True: 
        print("paolo")
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        print("paolo 2")
        print(f"sono in dip_o_zone {i}")
        
        finestra_attuale=frame_dip_o_zone
        bottone_attuale=button_back_dip_o_zone
        frame_admin.pack_forget()
        frame_dip_o_zone.pack()
        titolo_dip_zone=tk.CTkLabel(master=frame_dip_o_zone, text="SCEGLI QUALE TABELLA", font=("Roboto", 28))            
        titolo_dip_zone.pack()
        dip_bottone=tk.CTkButton(master=frame_dip_o_zone, text="DIPENDENTI", command=insert_dip, fg_color="Blue")
        dip_bottone.pack(side="right")
        zone_bottone=tk.CTkButton(master=frame_dip_o_zone, text="ZONE DI LAVORO",command=insert_zone,  fg_color="Red")            
        zone_bottone.pack(side="left")
    
        if flag_prima_VOLTA_dip_o_zone:
            print("La prima volta OMEGA")
            flag_prima_VOLTA_dip_o_zone = False
    else:
        
        frame_admin.pack_forget()
        frame_dip_o_zone.pack()




####################################################################################################################################################
def stampa_zone(): 
    global flag_prima_VOLTA_read_stampaZONE
    global finestra_attuale
    global bottone_attuale
    s.send("zone_di_lavoro".encode())

    frame_stampa_zone_new = tk.CTkFrame(master=root)  # Assuming 'root' is your main Tkinter window
    button_back_read_zone=tk.CTkButton(master=frame_stampa_zone_new, text="BACK", command=back_read, fg_color="Black")
    numero_iniziale_frame = len(root.winfo_children())
    print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
    finestra_attuale= frame_stampa_zone_new
    bottone_attuale=button_back_read_zone
    frame_read.pack_forget()
    frame_stampa_zone_new.pack()
    print("sono in stampa zone")
    s.send("zone_di_lavoro".encode())
    dati=s.recv(1024).decode()
    print(f"ricevo i {dati}")
    info=tk.CTkTextbox(master=frame_stampa_zone_new, width=400, corner_radius=0)
    info.insert("1.0", dati)
    info.pack()
    button_back_read_zone.pack()
    print("FINE !")
    '''
    if i==0 and flag_prima_VOLTA_read_stampaZONE: 
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        finestra_attuale= frame_stampa_zone
        bottone_attuale=button_back_read_zone
        frame_read.pack_forget()
        frame_stampa_zone.pack()
        print("sono in stampa zone")
        s.send("zone_di_lavoro".encode())
        dati=s.recv(1024).decode()
        print(f"ricevo i {dati}")
        info=tk.CTkTextbox(master=frame_stampa_zone, width=400, corner_radius=0)
        info.insert("1.0", dati)
        info.pack()
        button_back_read_zone.pack()
        print("FINE !")
        if flag_prima_VOLTA_read_stampaZONE:
            print("La prima volta ALPHA")
            flag_prima_VOLTA_read_stampaZONE = False
    else: 
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        frame_read.pack_forget()
        finestra_attuale= frame_stampa_zone
        bottone_attuale=button_back_read_zone
        frame_stampa_zone.pack()
        button_back_read_zone.pack()'''

        

def stampa_dip():
    s.send("dipendenti".encode())
    global flag_prima_VOLTA_read_stampaDIP
    global finestra_attuale
    global bottone_attuale

    # Create a new frame instance
    frame_stampa_dip_new = tk.CTkFrame(master=root)  # Assuming 'root' is your main Tkinter window
    button_back_read_dip = tk.CTkButton(master=frame_stampa_dip_new, text="BACK", command=back_read, fg_color="Black")
    numero_iniziale_frame = len(root.winfo_children())
    print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
    finestra_attuale = frame_stampa_dip_new
    bottone_attuale = button_back_read_dip
    frame_read.pack_forget()
    frame_stampa_dip_new.pack()
    label = tk.CTkLabel(master=frame_stampa_dip_new)
    print("sono entrato nella stampa")
    dati = s.recv(4096).decode() #i dati ricevuti sono incompleti perche i 1024 non bastano 
    print("ricevo i dati:", dati)
    info=tk.CTkTextbox(master=frame_stampa_dip_new, width=400, corner_radius=0)
    info.insert("1.0", dati)
    info.pack()
    button_back_read_dip.pack(pady=20, padx=20)
    print("FINE !")
    '''
    if i == 0 and flag_prima_VOLTA_read_stampaDIP:  # prima c'era i
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        finestra_attuale = frame_stampa_dip_new
        bottone_attuale = button_back_read_dip
        frame_read.pack_forget()
        frame_stampa_dip_new.pack()
        label = tk.CTkLabel(master=frame_stampa_dip_new)
        print("sono entrato nella stampa")
        dati = s.recv(1024).decode()
        print("ricevo i dati:", dati)
        info=tk.CTkTextbox(master=frame_stampa_dip_new, width=400, corner_radius=0)
        info.insert("1.0", dati)
        info.pack()
        button_back_read_dip.pack(pady=20, padx=20)
        print("FINE !")
        if flag_prima_VOLTA_read_stampaDIP:
            print("La prima volta ALPHA")
            flag_prima_VOLTA_read_stampaDIP = False

    else:
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        frame_read.pack_forget()
        frame_stampa_dip_new.pack()
        finestra_attuale = frame_stampa_dip_new
        bottone_attuale = button_back_read_dip
        button_back_read_dip.pack(pady=20, padx=20)'''


def read():
    global flag_prima_VOLTA_read
    global i
    global finestra_attuale
    global bottone_attuale
    s.send("R".encode())
    if i==0 or flag_prima_VOLTA_read: 
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        finestra_attuale = frame_read
        bottone_attuale= button_back_read
        frame_admin.pack_forget()
        frame_read.pack()
        button_back_read.pack()
        dip=tk.CTkButton(master=frame_read, command=stampa_dip, text="DIPENDENTI", fg_color="Blue") #ho aggiunto il lambda pk  senza utilizzare la lambda function, il che significa che la funzione viene eseguita immediatamente quando il pulsante "DIPENDENTI" viene creato, anziché quando viene effettivamente premuto il pulsante.
        dip.pack(pady=20, padx=20)
        zone=tk.CTkButton(master=frame_read, command=stampa_zone, text="ZONE DI LAVORO", fg_color="Red")
        zone.pack(pady=20, padx=20)
        if flag_prima_VOLTA_read:
            print("La prima volta ALPHA")
            flag_prima_VOLTA_read = False
    else: 
        numero_iniziale_frame = len(root.winfo_children())
        print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
        frame_admin.pack_forget()
        frame_read.pack()
        button_back_read.pack(pady=20, padx=20)


#modifiche fatte qui sotto, ricostruire il cod. butta giù j
#getsione entrata:       

def admin():
    try:
        global i
        if i == 0: #quidni entro la priaìma volta
            numero_iniziale_frame = len(root.winfo_children())
            print(f"Numero di frame nel root all'avvio: {numero_iniziale_frame}")
            frame_login.pack_forget()
            frame_admin.pack(pady=10, padx=10, fill='both', expand=True)
            label_admin = tk.CTkLabel(master=frame_admin, text="BENVENUTO ADMIN", font=("Roboto", 28))
            label_admin.pack(pady=18, padx=20)

            label_admin_scelta = tk.CTkLabel(master=frame_admin, text="QUALE OPERAZIONE VUOI ESEGUIRE: R-read, I-insert, D-delete, U-update", font=("Roboto", 16))
            label_admin_scelta.pack(pady=50, padx=50)
            

            bottone_read = tk.CTkButton(master=frame_admin, text="READ", command=read, fg_color="Red")
            bottone_read.pack(side="left", pady=5, padx=5)
            bottone_insert = tk.CTkButton(master=frame_admin, text="INSERT", command=dip_o_zone, fg_color="Blue")
            bottone_insert.pack(side="left", pady=5, padx=5)
            bottone_delete = tk.CTkButton(master=frame_admin, text="DELETE", command=dip_o_zone_delete, fg_color="Green")
            bottone_delete.pack(side="right", pady=5, padx=5)
            bottone_update = tk.CTkButton(master=frame_admin, text="UPDATE", command=dip_o_zone_update, fg_color="Purple")
            bottone_update.pack(side="right", pady=5, padx=5)
            bottone_quit=tk.CTkButton(master=frame_admin, text="ESCI", command=quit, fg_color="Black")
            bottone_quit.pack(side="bottom", pady=50)


        else:
            frame_admin.pack()
    except Exception as e:
        print(f"errorazzo de dio {e}")

def login():
    
    user_entry.get()
    print("SEI ENTRATO ! ")
    user = user_entry.get()
    password = password_entry.get()
    print(user, password)
    user = user.encode()
    password = password.encode()
    s.send(user)
    s.send(password)
    accesso = s.recv(1024).decode()
    print(f"{accesso}")
    if accesso == "True":
        try:
            admin()
        except Exception as e:
            print(e)

def show():
    frame_enter.pack_forget()
    frame_login.pack(pady=30, padx=90, fill="both", expand=True)
    label = tk.CTkLabel(master=frame_login, text="LOGIN DBMS", font=("Roboto", 28))
    label.pack(pady=18, padx=20)

    user_entry.pack(pady=18, padx=20)
    password_entry.pack(pady=18, padx=20)
    bottone = tk.CTkButton(master=frame_login, text="Login", command=login)
    bottone.pack(pady=18, padx=20)
    
#frame iniziali:
frame_enter.pack(pady=30, padx=90, fill="both", expand=True)
user_entry = tk.CTkEntry(master=frame_login, placeholder_text="username")
password_entry = tk.CTkEntry(master=frame_login, placeholder_text="password", show="*")
titolo = tk.CTkLabel(master=frame_enter, text="DBMS EINAUDI", font=("Roboto", 32))
titolo.pack(pady=24, padx=26)
enter = tk.CTkButton(master=frame_enter, text="Entra", command=show)
enter.pack(pady=24, padx=26)
path="C:\\Users\\hk450\\OneDrive\\Documenti\\python\\progetto GUI\\einaudi.jpeg"
img_einaudi= tk.CTkImage(Image.open(os.path.join(path)), size=(300,200)) #larghezza / lunghezza
immagine_einaudi=tk.CTkLabel(master=frame_enter, text="", image=img_einaudi)
immagine_einaudi.pack()

#bottoni: 
button_back_dip_o_zone= tk.CTkButton(master=frame_dip_o_zone, text="BACK", command=back, fg_color="Black")
button_back_dip_o_zone_del= tk.CTkButton(master=frame_dip_o_zone_del, text="BACK", command=back, fg_color="Black")
button_back_read = tk.CTkButton(master=frame_read, text="BACK", command=back, fg_color="Black")
button_back_insert_dip = tk.CTkButton(master=frame_insert_dip, text="BACK", command=back, fg_color="Black")
button_back_insert_zone = tk.CTkButton(master=frame_insert_zone, text="BACK", command=back, fg_color="Black")
button_back_delete = tk.CTkButton(master=frame_delete, text="BACK", command=back, fg_color="Black")
button_back_update = tk.CTkButton(master=frame_update, text="BACK", command=back, fg_color="Black")




#gestione delle connessione: 
HOST = 'localhost'
PORT = 50012
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
j=0
while True:
    if j==0:
        data = s.recv(1024)
        j+=1
        if data.decode() == "BENVENUTO NEL DBMS DELL'AZIENDA":
            try:
                root.mainloop()
            except Exception as e:
                print(e)
        else:
            print('Received: ', data.decode())
            testo = input("\ninserisci qualcosa: ").encode()
            s.send(testo)

s.close()


