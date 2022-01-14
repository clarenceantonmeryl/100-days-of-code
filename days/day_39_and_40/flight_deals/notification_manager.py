from twilio.rest import Client
import smtplib
TWILIO_PHONE = "+18646517397"
TWILIO_ACCOUNT_SID = "ACcf62378ca629ecc366e57ea9b642593a"
TWILIO_AUTH_TOKEN = "fd845e1b9849912c6a5ad129d75533e7"
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
EMAIL = "c.antonmeryl.123@gmail.com"
PASSWORD = "Almond123"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, destination, price):
        body = f"{destination} is available for flight for £{price}"
        message = self.client.messages \
            .create(
            body=body,
            from_=TWILIO_PHONE,
            to='+61499898919'
        )

        print(message.sid)

    def send_email(self, users, destination, price):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            for user in users:
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=user["email"],
                                    msg=f"Subject:Flight Found\n\n{destination} is available for flight for {price} GBP"
                                    )
