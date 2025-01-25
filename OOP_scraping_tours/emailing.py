import smtplib, os, imghdr
from email.message import EmailMessage

PASSWORD = os.getenv("PASSWORD")
SENDER = "kksharma011freelancing@gmail.com"
RECEIVER = "kksharma011freelancing@gmail.com"

class Email:
    def send(self, event_details):
        print("Send email function started")
        email_message = EmailMessage()
        email_message["Subject"] = "New Event!!!"
        email_message.set_content(f"Hey! New event {event_details}")

        

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
        gmail.quit()

        print("Send email function ended")

# if __name__ == "__main__":
#     send_email(image_path="images/10.png")