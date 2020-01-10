import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path  # https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'first_name last_name'
email['to'] = '<to email address>'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # print(email)
    smtp.login('<your email address>', '<your password>')
    smtp.send_message(email)
    print('all good boss!')
