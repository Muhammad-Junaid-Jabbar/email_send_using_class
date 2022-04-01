import os
import smtplib
from email.message import EmailMessage
from email.utils import COMMASPACE, formatdate

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

print(EMAIL_ADDRESS)


class SMTPEmail:
    """Email Library for Sending Mulipart Email using SMTP"""

    def __init__(self, server="smtp.gmail.com", port=587):
        self.msg = EmailMessage()
        self.server = server
        self.port = port

    """function for login to smtp"""

    def login(self, mail, password):
        """Login to SMTP Server"""
        self.send_from(mail)
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
        self.msg.set_content(text)

    def html_content(self, html):
        """HTML Email Message"""
        self.msg.add_alternative(html, subtype="html")

    @staticmethod
    def from_string(emp_str):
        a = emp_str.split(",")
        return a

    def attach_file(self, path):
        path = self.from_string(path)
        file_data = []
        file_name = []
        for file in path:
            with open(file, "rb") as f:
                file_data.append(f.read())
                file_name.append(f.name)
        print(file_name)
        print(file_data)
        for i in range(len(path)):
            self.msg.add_attachment(
                file_data[i],
                maintype="application",
                subtype="ocet-stream",
                filename=file_name[i],
            )

    def connect(self):
        self.server = smtplib.SMTP_SSL(self.server, self.port)

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
    with SMTPEmail("smtp.gmail.com", 465) as mail:
        # mail.send_from("admin@localhost")
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        # mail.send_from("raojunaidjabbar1999@gmail.com")
        mail.send_to("raojunaidjabbar1999@gmail.com")
        # mail.send_to("user@localhost")
        mail.subject("Test")
        mail.plain_content("Test Message")
        mail.html_content("<h1>Test Message</h1>")
        mail.attach_file("sample_text1.txt,pic.png")
        print(mail.message)
        mail.send()
