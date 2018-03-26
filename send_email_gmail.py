import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "from@gmail.com"#Change from Email
toaddr = "to@gmail.com"#Change To Email
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Subject email"

body = "Body of the email"
msg.attach(MIMEText(body, 'plain'))

filename = "file.txt"#Change Name File Email
attachment = open(r"C://Users/xxxx/Desktop/"+filename)#Change route file name

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "xxxxxxxx")#Put he password
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()