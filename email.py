import smtplib

email_id=input("sender email:")
email_receiver=input("receiver mail:")

subject=input("subject:")
message=input("message:")

text=f"subject:{subject}\n\n{message}"

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_id,"bqsd uhup lkhg oyjd")

server.sendmail(email_id,email_receiver,text)

print("email has been sent to "+email_receiver)
 

