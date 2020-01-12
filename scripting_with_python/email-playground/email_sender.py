import smtplib
from email.message import EmailMessage
from string import Template
# os.path  # https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'first_name last_name'
email['to'] = '<to email address>'
email['subject'] = 'Test for Instagram post on @dbergbrxkisez '

email.set_content(html.substitute({'name': '@dbergbrxkisez'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # print(email)
    smtp.login('<your email address>', '<your password>')
    smtp.send_message(email)
    print('all good boss!')
