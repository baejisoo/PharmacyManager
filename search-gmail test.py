import smtplib
from email.mime.text import MIMEText

def sendMail() :
    HOST = 'smtp.server.com'   # smtp 호스트 주소
    me = 'boat061114@gmail.com'     # 보내는 사람 메일 주소
    you = 'fanatic0717@naver.com'  # 받는 사람 메일 주소
    contents = '프로그램 뻗었다!!'

    msg = MIMEText(contents, _charset='euc-kr')
    msg['Subject'] = '[ALERT]'
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP(HOST)
    s.sendmail(me, [you], msg.as_string())
    s.quit()
