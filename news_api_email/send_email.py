import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kksharma011freelancing@gmail.com"
    password = os.getenv("PASSWORD")
    

    receiver = "kksharma011freelancing@gmail.com"
    context = ssl.create_default_context()
    # message = """\
    #     Subject: Hi!


    #     Hello 
    #     How are you
    #     """

    # message to be sent   
    # SUBJECT = "Hi"   
    # TEXT = """How are you? 
    # Bye!"""
    
    # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

