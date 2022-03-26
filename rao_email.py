import os
import smtplib
from email.message import EmailMessage


class SMTPEmail:
    """Email Library for Sending Mulipart Email using SMTP"""

    def __init__(self, server="smtp.gmail.com", port=587):
        self.msg = EmailMessage()
        self.server = server
        self.port = port
