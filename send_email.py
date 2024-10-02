import smtplib
import os


def email_function(message):
    host = "smtp.gmail.com"
    port = 465

    # Python Mega Course lecture 221 to set this up
    # email is also stored in environment variables
    username = os.getenv("EMAIL")

    # password is stored in environment variables
    # must restart computer after updating it
    password = os.getenv("PASSWORD")

    receiver = "moveshhh8@gmail.com"

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    email_function("Hello")
