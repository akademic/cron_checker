import smtplib
from email.mime.text import MIMEText

def notify(title, message, debug = False):
    if not debug:
        mail(['akademic@example.com', 'fiz@example.com'], title, message)
    else:
        mail(['debug@example.com'], title, message)

def mail(email, subject, body):
    me = 'watchdog@example.com'
    subject_prefix = ''
    message = MIMEText(body, 'plain', 'utf-8')
    message['Subject'] = subject_prefix+subject
    message['To'] = ', '.join(email)
    message['From'] = me

    s = smtplib.SMTP('localhost')
    s.sendmail(me, [email], message.as_string())
