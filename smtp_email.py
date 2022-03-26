import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate
from email.mime.application import MIMEApplication


class SMTPEmail:
    """Email Library for Sending Mulipart Email using SMTP"""

    def __init__(self, server="smtp.gmail.com", port=587, _ssl=False):
        self.msg = MIMEMultipart()

        self.server = server
        self.port = port
        self.ssl = _ssl

    def connect(self):
        if self.ssl:
            self.server = smtplib.SMTP_SSL(self.server, self.port)
        else:
            self.server = smtplib.SMTP(self.server, self.port)

    def login(self, mail, password, tls=True):
        """Login to SMTP Server"""
        self.send_from(mail)
        if tls:
            self.server.starttls()
            self.server.ehlo()

        self.server.login(mail, password)

    def close(self):
        self.server.close()

    def send_from(self, mail: str):
        """Send From or Sender Email"""
        self.msg["From"] = mail

    def send_to(self, mail):
        """Send to Email or List of Emails"""
        if isinstance(mail, str):
            self.msg["To"] = mail
        else:
            self.msg["To"] = COMMASPACE.join(mail)

    def subject(self, subject: str):
        self.msg["Subject"] = subject

    def plain_content(self, text):
        """Plain Text Message"""
        self.msg.attach(MIMEText(text, _subtype="plain"))

    def html_content(self, html):
        """HTML Email Message"""
        self.msg.attach(MIMEText(html, _subtype="html"))

    def attach_image(self, path):
        """Attach Image file as Attachment"""
        with open(path, "rb") as f:
            part = MIMEImage(f.read())
            part.add_header(
                "Content-Disposition", "attachment", filename=os.path.basename(path)
            )
            self.msg.attach(part)

    def attach_audio(self, path):
        """Attach Audio file as Attachment"""
        with open(path, "rb") as f:
            part = MIMEAudio(f.read())
            part.add_header(
                "Content-Disposition", "attachment", filename=os.path.basename(path)
            )
            self.msg.attach(part)

    def attach_file(self, path):
        """Attach Normal file as Attachment"""
        with open(path, "rb") as f:
            part = MIMEApplication(f.read())
            part.add_header(
                "Content-Disposition", "attachment", filename=os.path.basename(path)
            )
            self.msg.attach(part)

    def add_image(self, path, name):
        """Add Image for use in HTML <img src="cid:name">"""

        with open(path, "rb") as f:
            part = MIMEImage(f.read())
            part.add_header(
                "Content-Disposition", "inline", filename=os.path.basename(path)
            )
            part.add_header("Content-ID", f"<{name}>")
            self.msg.attach(part)

    @property
    def message(self) -> str:
        """Get Message as String"""
        return self.msg.as_string()

    def send(self, localtime=True):
        """Send Email"""
        self.msg["Date"] = formatdate(localtime=localtime)
        self.server.send_message(self.msg)

    def __enter__(self):
        """Context Manager Enter Method"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Context Manager Exit Method"""
        self.close()


if __name__ == "__main__":
    """Example"""
    with SMTPEmail("smtp.gmail.com", 587, _ssl=False) as mail:
        # mail.send_from("admin@localhost")
        # mail.login("raojunaidjabbar1999@gmail.com", "Fahaduser88", tls=True)
        # mail.send_from("raojunaidjabbar1999@gmail.com")
        mail.send_to("raojunaidjabbar1999@gmail.com")
        # mail.send_to("user@localhost")
        mail.subject("Test")
        mail.plain_content("Test Message")
        mail.html_content("<h1>Test Message</h1>")
        mail.attach_file("/home/rao/test_mail.txt")
        print(mail.message)
        mail.send()
