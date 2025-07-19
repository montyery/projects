import pandas as pd
import datetime
import smtplib

email_id = input("Enter your email ID: ")
email_password = input("Enter your app password: ")
#pass=zhuh hemj obce sphs

def sendmail(to, sub, msg):
    print(f"Sending email to {to} with subject: {sub}")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_id, email_password)
    server.sendmail(email_id, to, f"Subject: {sub}\n\n{msg}")
    server.quit()

if __name__ == "__main__":
    
    df = pd.read_excel("data.csv.xlsx", usecols=['BIRTHDAY', 'mail', 'DIALOGUE'])

    today = datetime.datetime.now().strftime("%d-%m")

    sent = False
    for index, item in df.iterrows():
        bday = item['BIRTHDAY'].strftime("%d-%m")
        if today == bday:
            sendmail(item['mail'], "Happy Birthday!", item['DIALOGUE'])
            print("Email has been sent to " + item['mail'])
            sent = True

    if not sent:
        print("Oops, today is nobody's birthday.")
