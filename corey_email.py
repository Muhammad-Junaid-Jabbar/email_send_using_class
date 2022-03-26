import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

contacts = ["YourAddress@gmail.com", "test@example.com"]
emails = [EMAIL_ADDRESS, "raojunaidjabbar1999h@gmail.com"]
msg = EmailMessage()
msg["Subject"] = "Check out Bronx as a puppy!"
msg["From"] = EMAIL_ADDRESS
msg["To"] = emails
msg.set_content("This is a plain text email")

msg.add_alternative(
    """\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""",
    subtype="html",
)
with open("pic.png", "rb") as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(
        file_data, maintype="application", subtype="ocet-stream", filename=file_name
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
