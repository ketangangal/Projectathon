import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_sender(receiver_email, logger):
    try:
        sender = "ketangangal98@gmail.com"
        my_password = 'dfdw yazr ckiy pjqu'
        receiver = receiver_email

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "SIMPLIFIED AI : Process Completed"
        msg['From'] = sender
        msg['To'] = receiver

        html = '<html><body><p>Hello, Your process has been completed please download the resouces!</p></body></html>'
        part2 = MIMEText(html, 'html')

        msg.attach(part2)
        s = smtplib.SMTP_SSL('smtp.gmail.com')
        s.login(sender, my_password)

        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        return True
    except Exception as e:
        return e.__str__()
