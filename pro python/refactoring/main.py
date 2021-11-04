from refact_class import email

if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None
    person = email(login, password)
    person.send(recipients, subject, message)
    person.receive(header)