import sys
import chilkat

imap = chilkat.CkImap()

# This example assumes Chilkat Imap to have been previously unlocked.
# See Unlock Imap for sample code.

# Connect to an IMAP server.
# Use TLS
imap.put_Ssl(False)
imap.put_Port(993)
success = imap.Connect("mail.ita.locaweb.com.br")
if (success != True):
    print(imap.lastErrorText())
    sys.exit()

# Login
success = imap.Login("admrh@acarape.ce.gov.br","Acarape@ssesi26")
if (success != True):
    print(imap.lastErrorText())
    sys.exit()

sbMime = chilkat.CkStringBuilder()
sbMime.LoadFile("Inbox/b'1'.eml","utf-8")

# Upload to the mailbox.
success = imap.AppendMime("INBOX" ,sbMime.getAsString())
if (success != True):
    print(imap.lastErrorText())
    sys.exit()

imap.Disconnect()

print("OK.")