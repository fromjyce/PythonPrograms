import smtplib

#Outlook Must

SENDER_EMAIL = " "
SENDER_PASSWORD = " "
def send_email(rec_mail,subject,body):
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP("smtp.office365.com",587) as server:
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,rec_mail,message)

rec_mail  = " " #Receiver's Mail Address
send_email(rec_mail,"Notification","Everything is awesome")