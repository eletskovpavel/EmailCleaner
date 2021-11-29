import imaplib
import email
import email.message
from email.header import decode_header

#Данные для авторизации в почтовом ящике Gmail
mailbox = "angelinaturaeva26@gmail.com"
password = "xbbabjstmwebokmm"



def deleteMessagesFromOneSender(sender): 
    status, select_data = imap.select('INBOX')
    nmessages = select_data[0].decode('utf-8')
    status, search_data = imap.search(None, 'ALL')
    for msg_id in search_data[0].split():
        msg_id_str = msg_id.decode('utf-8')
        print ("Fetching message {} of {}".format(msg_id_str,nmessages))
        status, msg_data = imap.fetch(msg_id, '(RFC822)')
        msg_raw = msg_data[0][1]
        msg = email.message_from_bytes(msg_raw, _class = email.message.EmailMessage)
        msgSender = str(msg['From'])
        if  msgSender.__contains__(sender):
            imap.store(msg_id, '+FLAGS', '\\Deleted')


def printSenders():
    arrayOfSenders = []
    status, select_data = imap.select('INBOX')
    nmessages = select_data[0].decode('utf-8')
    status, search_data = imap.search(None, 'ALL')
    for msg_id in search_data[0].split():
        msg_id_str = msg_id.decode('utf-8')
        print ("Fetching message {} of {}".format(msg_id_str,nmessages))
        status, msg_data = imap.fetch(msg_id, '(RFC822)')
        msg_raw = msg_data[0][1]
        msg = email.message_from_bytes(msg_raw, _class = email.message.EmailMessage)
        msgSender = str(msg['From'])
        if arrayOfSenders.__contains__(msgSender):
            continue
        else:
            arrayOfSenders.append(msgSender)
    fileOne = open('Senders.txt','w')
    for element in arrayOfSenders:
        fileOne.write(element + '\n')

mailbox = input('Введите Ваш почтовый ящик gmail: ')
password = input('Введите Ваш пароль к почтовому приложению: ')

imap = imaplib.IMAP4_SSL("imap.gmail.com",993)
imap.login(mailbox,password)

def choise():
    while True:
        action = int(input('Для записи отправителей в файл нажмите 1, для удаления сообщений одного отправителя нажмите 2: '))
        if action == 1:
            printSenders()
            break
        elif action == 2:
            senderIn = input('Введите отправителя, письма которого вы хотите удалить: ')
            deleteMessagesFromOneSender(senderIn)
            break
        else:
            print('Введен неверный вариант, в следующий раз введите 1 или 2')
            continue

choise()

imap.expunge()
imap.logout()
                
        
    


