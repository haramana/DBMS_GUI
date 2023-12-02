import threading 
import socket
import mysql.connector
import smtplib_mail as mail
import txt_converter as txt
import hash_function as h
import time
path = r'C:\\Users\\hk450\\OneDrive\Documenti\\python\\PROGETTO GUI\\database.txt'

db_lock=threading.Lock()


#variabili globali: 
comunicazioni = ["",""]
PASSWORD = "CIAO"
USERNAME= "ADMIN"



def gestisci_comunicazione(conn):
    try: 
        conn.send("BENVENUTO NEL DBMS DELL'AZIENDA".encode())
        #conn.send("Benvenuto, inserisci l'username: ".encode())
        user = conn.recv(1024).decode()
        #conn.send("Benvenuto, inserisci password: ".encode())
        password = conn.recv(1024).decode()
        
        entry=login(user, password)

        i=0
        if entry is False: 
            while password != PASSWORD and user != USERNAME and i<2:
                i+=1
                conn.send("ERRORE ! premi invio per continuare ".encode())
                conn.send("Benvenuto, inserisci l'username: ".encode())
                user = conn.recv(1024).decode()
                conn.send(f"Password ERRATA, reinserisci password: (numero tentativo {i+1}) ".encode())
                password= conn.recv(1024).decode()

                entry=login(user, password) # RICORSIVA
            if password !=PASSWORD and user != USERNAME: 
                conn.send("STOP".encode())
                conn.close()
                return

        while entry:
            seconds = time.time()
            print("Time in seconds since the epoch:", seconds)
            conn.send("True".encode()) # mando il true a client per la funzione login()
            data= conn.recv(1024).decode() # ricevo la scelta
            print(data)
            #read
            if data.upper() == "R":
                print("IO SONO QUI MA MI BLOCCO PERCHE?")
                #conn.send("vuoi vedere la tabella dipendenti o la tabella zone_di_lavoro? ".encode())
                scelta=conn.recv(1024).decode()
                if scelta.upper()=="DIPENDENTI": 
                    scelta+="_harman_singh "
                    #print(scelta)
                    scelta= scelta.strip()
                    dati_query= db_get(scelta)
                    print("returna questo la funzione: --> ", dati_query)
                    #LA FUNZIONE DATI_QUERY nel server returna delle stringhe ma al client arriva un valore booleano
                    #quindi usi json
                    # dati_query = db_get(scelta)
                    #dati_json = json.dumps(dati_query)
                    #conn.send(dati_json.encode()) 

                    conn.send(str(dati_query).encode())
                    #txt.crea_file(path, dati_query)
                elif scelta.upper() == "ZONE_DI_LAVORO": 
                    scelta+="_harman_singh "
                    #print(scelta)
                    scelta=scelta.strip() # serve per togliere gli spazi se no il comando non viene eseguito
                    dati_query=db_get(scelta)
                    conn.send(str(dati_query).encode())
            #insert
            elif data.upper() == "I":
                with db_lock:
                    #conn.send("vuoi inserire nella tabella dipendenti oppure zone di lavoro: ".encode())
                    scelta=conn.recv(1024).decode()
                    print(scelta)
                    if scelta.upper() == "DIPENDENTI":
                        print("GUI 1") 
                    
                        print(scelta)
                        nome=conn.recv(1024).decode()
                        print(nome)
                        cognome=conn.recv(1024).decode()
                        print(cognome)
                        pos_lavorativa=conn.recv(1024).decode()
                        print(pos_lavorativa)
                        data_assunzione=conn.recv(1024).decode()
                        print(data_assunzione)
                        eta=conn.recv(1024).decode()
                        print(eta)
                        ind=conn.recv(1024).decode()
                        print(ind)
                        scelta+= "_harman_singh"
                        scelta=scelta.strip()
                        print("scelta: ", scelta)
                        print(f"dati: {nome, cognome, pos_lavorativa, data_assunzione, eta, ind}")
                        try:
                            print("CIAO")
                            dati_query= db_insert_dipendenti(scelta, nome, cognome, pos_lavorativa, data_assunzione, eta, ind,)
                            #non invio 
                            conn.send(dati_query.encode())
                        except Exception as e: 
                            print(f"errore insert: {e}")

                        
                    elif scelta.upper() == "ZONE_DI_LAVORO": 
                        print("SONO IN ZONE GANG")
                        zona=conn.recv(1024).decode()
                        clienti=conn.recv(1024).decode()
                        id_dip=conn.recv(1024).decode()
                        reparto=conn.recv(1024).decode()
                        scelta+="_harman_singh"
                        scelta=scelta.strip()
                        print(f"dati: {zona, clienti, id_dip, reparto}")
                        try:
                            dati_query= db_insert_zone(scelta, zona, clienti, id_dip, reparto)
                        except Exception as e: 
                            print(f"ERRORE INSERIMENTO ZONE: {e}")


            #delete: 
            elif data.upper() == "D" :
                with db_lock:
                    
                    scelta= conn.recv(1024).decode()
                    print(":::", scelta)
                    if scelta.upper() == "DIPENDENTI": 

                        #conn.send("Inserisci l'id del dipendente da eliminare ?".encode())
                        id=conn.recv(1024).decode()
                        id=int(id)
                        print("ID", id)
                        scelta+="_harman_singh"
                        dati_query=db_eleminare_dipendenti(scelta, id)
                    elif scelta.upper() == "ZONE_DI_LAVORO":
                        print("sono in zone di lavoro") 
                        id_zona=conn.recv(1024).decode()
                        scelta+="_harman_singh"
                        id_zona=int(id_zona)
                        dati_query= db_eliminare_zone(scelta, id_zona)
                    
            
            elif data.upper() == "U":
                with db_lock:
                
                    #conn.send("In quale tabella vuoi modificare: dipendenti oppure zone_di:lavoro ".encode())
                    scelta= conn.recv(1024).decode()

                    if scelta.upper() == "DIPENDENTI":
                        #conn.send("Inserisci ID del dipendente a cui vuoi apportare le modifiche: ".encode())
                        update_id= conn.recv(1024).decode()
                        #conn.send("inserisci il nome: ".encode())
                        nome= conn.recv(1024).decode()
                        #conn.send("inserisci il cognome: ".encode())
                        cognome= conn.recv(1024).decode()
                        #conn.send("inserisci la posizione lavorativa: ".encode())
                        pos_lavorativa= conn.recv(1024).decode()
                        #conn.send("inserisci la data di assunzione: AA/MM/GG ".encode())
                        data_assunzione= conn.recv(1024).decode()
                        #conn.send("inserisci l'eta: ".encode())
                        eta= conn.recv(1024).decode()
                        eta=int(eta)
                        #conn.send("inserisci l'indirizzo: ".encode())
                        ind=conn.recv(1024).decode()
                        scelta+="_harman_singh"
                        scelta= scelta.strip()
                        dati_query= db_update_dip(scelta, nome,cognome, pos_lavorativa, data_assunzione, eta, ind, update_id)
                        
                    elif scelta.upper() == "ZONE_DI_LAVORO": 
                        #conn.send("Inserisci ID ZONA da modificare: ".encode())
                        scelta_id= conn.recv(1024).decode()
                        #conn.send("inserisci il nome della zona: ".encode())
                        zona=conn.recv(1024).decode()
                        #conn.send("inserisci il numero di clienti: ".encode())
                        clienti=conn.recv(1024).decode()
                        clienti=int(clienti)
                        #conn.send("inserisci il id del dipendente: ".encode())
                        id_dip=conn.recv(1024).decode()
                        #conn.send("inserisci il reparto: ".encode())
                        reparto=conn.recv(1024).decode()
                        scelta+="_harman_singh"
                        scelta=scelta.strip()
                        dati_query= db_update_zone(scelta, zona, clienti, id_dip, reparto, scelta_id)
                   
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.close()

# FUNZIONE CREATA PER BLOCCARE ATTACCHI MYSQL INJECTION DI TIPO DIRECT
def login(user, passWORD): 

    conn= mysql.connector.connect(

        host= "127.0.0.1", 
        user="harman_singh",
        password="harman1234",
        database="5ATepsit", 
        port=3306,
    )
    cur = conn.cursor(prepared=True)
    print("ci sono")
    '''
    LE PASSWORD ALL'INTERNO DEL DB NON VENGONO SALVATE IN CHIARO MA VENGONO SALVATI I VALORI HASH
    la funzione 'pass_to_hash' serve per calcolare il valore hash della password inserita dal client. 

    '''
    password=h.pass_to_hash(passWORD)
    try:
        #cur.execute(f"SELECT * FROM utenti WHERE username LIKE '{user}' AND identification LIKE '{password}' ")
        #QUESTA RIGA SOFFRE DALL'ATTACCO MYSQL INJECTION PERCHÉ INSERIMENTO DI TIPO : 
        # admin' OR '1' = '1 oppure admin' -- vanno a lanciare istruzioni mysql evasive che permettono l'accesso non autorizzato
        #basta fare un' escape delle stringhe: 
        cur.execute("SELECT * FROM utenti WHERE username = %s  AND identification = %s ", (user, password)) 
        if cur.fetchall():
            print("ci sono 2")
            return True
        else: 
            return False
    except Exception as e: 
        return False

###########################################################################################################################################

def db_get(scelta):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="harman_singh",
        # per db scuola: password="singh1234",
        password= "harman1234",
        database="5ATepsit",
        port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
        )

    cur = conn.cursor(prepared=True) # per prevenire comandi sql

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    if scelta == "dipendenti_harman_singh": 
        print("questa volta non mi so bloccato godo")
        query = f"SELECT * FROM {scelta} "
        cur.execute(query)
        dati = cur.fetchall()
        print(dati) 
        return dati
    elif scelta == "zone_di_lavoro_harman_singh": 
        query= f"SELECT * FROM {scelta} "
        cur.execute(query)
        dati= cur.fetchall()
        print(dati)
        return dati

##########################################################################################################################################

def db_insert_dipendenti(scelta, nome, cognome, pos, data, eta, ind): 
    conn= mysql.connector.connect(
        host="127.0.0.1",
        user="harman_singh",
        password="harman1234",
        database="5Atepsit",
        port=3306
    )

    cur= conn.cursor(prepared=True)  # per prevenire comandi sql
    print("ciao1")
    if scelta == "dipendenti_harman_singh":
        print("ciao2")
        insert_query= f"INSERT INTO dipendenti_harman_singh (nome, cognome, posizione_lavorativa, data_assunzione, eta, indirizzo) VALUES (%s, %s, %s, %s, %s, %s)"
        values=(nome, cognome, pos, data, eta, ind, )
        try: 
            print("ciao3")
            cur.execute(insert_query,values)
            conn.commit()  # Commit delle modifiche nel database
            print("ciao4")
            print(f"INSERIMENTO RIUSCITO")
            seconds = time.time()
            print("Time in seconds since the epoch:", seconds)
        
        except Exception as e: 
            print(f"Errore durante l'inserimento: {e}")
            conn.rollback()   # In caso di errore, effettua il rollback delle modifiche
    

##########################################################################################################################################     

def db_insert_zone(scelta, nome_zona, num_clienti, id_dip, rep): 
    conn= mysql.connector.connect(
        host="127.0.0.1",
        user="harman_singh",
        password="harman1234",
        database="5Atepsit",
        port=3306
    )

    cur= conn.cursor(prepared= True)  # per prevenire comandi sql
    print("ciao1")
    if scelta == "zone_di_lavoro_harman_singh": 
        insert_query= f"INSERT INTO zone_di_lavoro_harman_singh (nome_zona, numero_clienti, id_dipendente, reparto) VALUES (%s, %s, %s, %s)"
        values= (nome_zona, int(num_clienti), id_dip, rep, )
        try: 
            cur.execute(insert_query, values)
            conn.commit()
            print(f"INSERIMENTO RIUSCITO")
        except Exception as e: 
            print(f"Errore durante l'inserimento: {e}")
            conn.rollback()


##########################################################################################################################################

def db_eleminare_dipendenti(scelta, id): 
    print("Sono nella funzione")
    conn=mysql.connector.connect(
        host="127.0.0.1",
        user="harman_singh",
        password="harman1234",
        database="5Atepsit",
        port=3306
    )
    cur= conn.cursor(prepared=True) 
    if scelta == "dipendenti_harman_singh": 
        insert_query= f"DELETE FROM dipendenti_harman_singh WHERE id = %s"
        values=(id, )
        print("query: ", insert_query)
        try: 
            print("sono nel delete")
            cur.execute(insert_query, values)
            conn.commit()
            print("DELETE RIUSCITO")
            try: 

                mail.manda_mail_dip()
            except Exception as e:
                print(f"Errore durante l'eliminazione: {e}")

        except Exception as e: 
            print(f"Errore durante l'eliminazione: {e}")
            conn.rollback()
    
##########################################################################################################################################

def db_eliminare_zone(scelta, id): 
    conn= mysql.connector.connect(
        host="127.0.0.1",
        user="harman_singh",
        password="harman1234",
        database="5Atepsit",
        port=3306

    )
    cur= conn.cursor(prepared=True)


    if scelta=="zone_di_lavoro_harman_singh": 
        print("wewe")
        insert_query_zona=f"DELETE FROM zone_di_lavoro_harman_singh WHERE id_zona = %s"
        values=(id, )
        try: 
            print("wewe2")
            cur.execute(insert_query_zona, values)
            conn.commit()
            try: 
                mail.manda_mail_zona()
            except Exception as e: 
                print(f"ERRORE: {e}")

            print("wewe3")
            print("ELIMINAZIONE RIUSCITA")
        except Exception as e: 
            print(f"ERRORE DURANTE L'ELIMINAZIONE: {e}")
            conn.rollback()

##########################################################################################################################################

def db_update_dip(scelta, nome, cognome, pos_lavorativa, data, eta, ind, update_id):

    conn= mysql.connector.connect(

        host= "127.0.0.1",
        user= "harman_singh", 
        password="harman1234",
        database="5Atepsit",
        port=3306

    ) 
    cur= conn.cursor(prepared=True)

    query= f" UPDATE dipendenti_harman_singh SET nome = %s, cognome = %s, posizione_lavorativa = %s, data_assunzione = %s, eta = %s, indirizzo = %s WHERE id = %s "
    values=(nome, cognome, pos_lavorativa, data, eta, ind, update_id, )

    try: 
        cur.execute(query, values)
        conn.commit()
        print("UPDATE RIUSCITO")
    except Exception as e: 
        print(f"ERRORE UPDATE: {e}")
        conn.rollback()

def db_update_zone(scelta, zona, clienti, id_dip, reparto, scelta_id):

    conn=mysql.connector.connect(
        host= "127.0.0.1",
        user= "harman_singh", 
        password="harman1234",
        database="5Atepsit",
        port=3306
    )
    cur=conn.cursor(prepared=True)
    query= f"UPDATE zone_di_lavoro_harman_singh SET nome_zona = %s, numero_clienti = %s, id_dipendente = %s, reparto = %s WHERE id_zona = %s "

    values= (zona, clienti, id_dip, reparto, scelta_id, )
    try: 
        cur.execute(query, values, )
        conn.commit()
        print("UPDATED ")
    except Exception as e: 
        print(f"ERRORE UPDATE {e}")
        conn.rollback()


#gestione dei client in accesso ai server:

print("server in ascolto: ")
lock = threading.Lock()
HOST = ''                 # Nome simbolico che rappresenta il nodo locale, ci va l'indirizzo IP
PORT = 50012        # Porta non privilegiata arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i=0

while True:
    lista_connessioni.append( s.accept() ) #connessione = s.accept() 
    print('Connected by', lista_connessioni[i][1]) # print(connessione[0])
    thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) )) 
    thread[i].start()
    i+=1

