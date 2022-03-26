import yagmail
import sys


class email:

    # Initialize email parameters
    def __init__(self, receiver=[], sender="", subject="", body="", attachments=[]):
        self.receiver = receiver
        self.sender = sender
        self.subject = subject
        self.body = body
        self.attachments = attachments

    # if user enter multiple inputs like sender names and attachments with ',' separator
    @staticmethod
    def from_string(emp_str):
        a = emp_str.split(",")
        return a

    # set the sender email
    @staticmethod
    def send_email(self):
        try:
            yag = yagmail.SMTP(self.sender)
            if self.attachments == []:
                self.attachments = None
            yag.send(
                to=self.receiver,
                subject=self.subject,
                contents=self.body,
                attachments=self.attachments,
            )
            print("email sent")
        except:
            print("sender email error")

    @staticmethod
    def check():
        x = str(input("do you want another email to send yes/no:/y/n---> "))
        x = x.lower()
        if x == "no" or x == "n":
            sys.exit("thanks")


while True:
    print("<--------------------------------------------------------------------->")
    print("                    <---Email Sending Program--->                      ")
    sender = input("Enter sender mail--->")
    print(" ---if multiple receiver email addresses, then use ',' for separator---")
    receiver = input("Enter receiver mail--->")
    receiver = email.from_string(receiver)

    subject = input("Enter the subject of email--->")
    body = input("Enter the body of email--->")
    attach = input("Enter path of attachments--->")
    attach = email.from_string(attach)

    email1 = email(
        sender=sender, receiver=receiver, body=body, subject=subject, attachments=[]
    )

    email.send_email(email1)

    email.check()
