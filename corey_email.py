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
a = ["sample_text1.txt", "sample_text2.txt", "pic.png"]
# i = -1
file_data = []
file_name = []
for file in a:

    with open(file, "rb") as f:
        file_data.append(f.read())
        file_name.append(f.name)
# print(file_name)
# print(file_data)
for i in range(len(a)):

    msg.add_attachment(
        file_data[i],
        maintype="application",
        subtype="ocet-stream",
        filename=file_name[i],
    )

# with open("a.txt", "rb") as f:
#     file_data1 = f.read()
#     file_name1 = f.name
#     msg.add_attachment(
#         file_data1, maintype="application", subtype="ocet-stream", filename=file_name1
#     )
print(EMAIL_ADDRESS)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    #print(msg.as_string())
    print(msg)
