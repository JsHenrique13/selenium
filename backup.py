import sys
import imaplib
import getpass

IMAP_SERVER = "138.128.166.178"
EMAIL_ACCOUNT = "admrh@acarape.ce.gov.br"
EMAIL_FOLDER = "Inbox"
OUTPUT_DIRECTORY = 'Inbox'
IMAP_SERVER1 = "mail.ita.locaweb.com.br"
PASSWORD = "Acarape@ssesi26"


def process_mailbox(M):
    """
    Dump all emails in the folder to files in output directory.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print ("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print ("ERROR getting message", num)
            return
        print ("Writing message ", num)

        f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, num), 'wb')
        f.write(data[0][1])
        f.close()


def main():
    M = imaplib.IMAP4_SSL(IMAP_SERVER)
    M.login(EMAIL_ACCOUNT, PASSWORD)
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        print ("Processing mailbox: ", EMAIL_FOLDER)
        process_mailbox(M)
        M.close()
    else:
        print ("ERROR: Unable to open mailbox ", rv)
    M.logout()


def teste():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER1)
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    data = open("Inbox/b'1'.eml",'rb') 
    rv, data = mail.select("./")
    try:    
        mail.send(b"Inbox/b'1'.eml")
        
    except Exception as e:
        print("erro", e)
    mail.logout()

if __name__ == "__main__":
    teste()