# importing the Yagmail library
import yagmail

try:
    # initializing the server connection
    yag = yagmail.SMTP(
        # required to bypass email format validation
        user={"INSERT MAILTRAP USERNAME": ""},  # Mailtrap username
        soft_email_validation=False,
        password="INSERT MAILTRAP PASSWORD",  # Mailtrap password
        host="smtp.mailtrap.io",
        smtp_starttls=True,
        smtp_ssl=False,
    )
    # sending the email
    # yag.send(to='user1@gmail.com', subject='Mailtrap and Yagmail', contents='The testing worked!')
    print("Email sent successfully")
except:
    print("Error, email was not sent")
