# -*- coding: cp949 -*-

import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

class sendMail():
    #global value
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.html"

    senderAddr = input("보내는 사람 Gmail 입력: ")     # 보내는 사람 email 주소.
    senderPw = input("보내는 사람 Gmail 비밀번호 입력: ")
    recipientAddr = input("Email 입력: ")   # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Test email(Pharmacy Manager) in Python 3.0"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
    htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr,senderPw)
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
