import smtplib as smtp
import datetime
def manda_mail_dip():
    data_ora_cancellazione = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    oggetto_mail = "Subject: ELIMINAZIONE DI UN RECORD NEL DATABASE \n\n"
    contenuto_mail= f'''Ti scrivo per informarti che è stata effettuata una cancellazione nel nostro database relativa al record di un dipendente.\nQuesto processo è stato eseguito in seguito a una richiesta da parte del dipendente stesso o del suo superiore autorizzato.\n
                    Ecco i dettagli relativi alla cancellazione:\n
                    -data e ora della cancellazione: {data_ora_cancellazione}. \n
                    Per garantire la trasparenza e la tracciabilità, abbiamo mantenuto una copia dei dati del dipendente cancellato in un archivio sicuro per un periodo specifico di conformità, come richiesto dalla legge e dalle normative aziendali.\n
                    Se hai domande o hai bisogno di ulteriori informazioni sulla cancellazione del record del dipendente, ti preghiamo di rispondere a questa email o di contattarci telefonicamente.\n
                    Grazie per la tua attenzione a questa questione. La sicurezza e la gestione accurata dei dati dei dipendenti sono una priorità per noi, e siamo sempre a tua disposizione per qualsiasi assistenza di cui tu possa aver bisogno.\n
                    Cordiali saluti,'''

    messaggio = str(oggetto_mail + contenuto_mail).encode('utf-8')  # Codifica il messaggio in UTF-8

    mail_server = "smtp.gmail.com"
    port_mail_server = 587

    mail = "database.eventmanager@gmail.com"
    password = "qaqn qnlw nvlg dphn"
    destination_email = "singh.harman@einaudicorreggio.it"

    email = smtp.SMTP(mail_server, port_mail_server)
    email.ehlo()
    email.starttls()
    email.login(mail, password)  # Non è necessario codificare la password

    email.sendmail(mail, destination_email, messaggio)

    email.quit()

def manda_mail_zona():
    data_ora_cancellazione = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    oggetto_mail = "Subject: ELIMINAZIONE DI UN RECORD NEL DATABASE \n\n"
    contenuto_mail= f'''Ti scrivo per informarti che è stata effettuata una cancellazione nel nostro database relativa al record di una zona.\nQuesto processo è stato eseguito in seguito a una richiesta da parte del dipendente stesso o del suo superiore autorizzato.\n
                    Ecco i dettagli relativi alla cancellazione:\n
                    -data e ora della cancellazione: {data_ora_cancellazione}. \n
                    Per garantire la trasparenza e la tracciabilità, abbiamo mantenuto una copia dei dati della zona cancellata in un archivio sicuro per un periodo specifico di conformità, come richiesto dalla legge e dalle normative aziendali.\n
                    Se hai domande o hai bisogno di ulteriori informazioni sulla cancellazione del record della zona, ti preghiamo di rispondere a questa email o di contattarci telefonicamente.\n
                    Grazie per la tua attenzione a questa questione. La sicurezza e la gestione accurata dei dati delle zone sono una priorità per noi, e siamo sempre a tua disposizione per qualsiasi assistenza di cui tu possa aver bisogno.\n
                    Cordiali saluti,'''

    messaggio = str(oggetto_mail + contenuto_mail).encode('utf-8')  # Codifica il messaggio in UTF-8

    mail_server = "smtp.gmail.com"
    port_mail_server = 587

    mail = "database.eventmanager@gmail.com"
    password = "qaqn qnlw nvlg dphn"
    destination_email = "singh.harman@einaudicorreggio.it"

    email = smtp.SMTP(mail_server, port_mail_server)
    email.ehlo()
    email.starttls()
    email.login(mail, password)  # Non è necessario codificare la password

    email.sendmail(mail, destination_email, messaggio)

    email.quit()


        