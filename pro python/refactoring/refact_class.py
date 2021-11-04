import email
import smtplib
import imaplib

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class email:
    def __init__(self, login, password) -> None:
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.login = login
        self.password = password

    def send(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()   # identify ourselves to smtp gmail client   
        ms.starttls()   # secure our email with tls encryption
        ms.ehlo()   # re-identify ourselves as an encrypted connection
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()
    
    def receive(self, header):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

