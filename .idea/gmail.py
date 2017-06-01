import email
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소
port = "587"
htmlFileName = "logo.html"

senderAddr = "prof.boat061114@gamail.com"
recipientAddr = "fanatic0717@naver.com"

msg=MIMEBase("multipart", "alternative")
msg['Subject']="Test email in Python 3.5"
msg['From']=senderAddr
msg['To']=recipientAddr

#MIME 문서를 생성합니다.
htmlFD = open(htmlFileName, 'rb')
HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8')
htmlFD.close()

#만들었던 mime을 MIMEBase에 첨부 시킨다.
msg.attach(HtmlPart)

#메일을 발송한다.
s = mysmtplib.MySMTP(host, port)
#s.set debuglevel(1)        #디버깅이 필요할 경우 주석을 푼다.
s.ehlo()
s.starttls()
s.ehlo()
s.login("prof.boat061114@gmail.com", "wltn0412")
s.sendmail(senderAddr, [recipientAddr], msg.as_string())
s.close()
