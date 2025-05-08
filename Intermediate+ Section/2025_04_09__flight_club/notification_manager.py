import smtplib
GMAIL_EMAIL = "smpythonproject@gmail.com"
GMAIL_APP_PASSWORD = ""
YAHOO_EMAIL = "smpythonproject@yahoo.com"

class NotificationManager:

    def __init__(self):
        # Retrieve environment variables only once
        self.to_email = YAHOO_EMAIL
        self.email = GMAIL_EMAIL
        self.email_password = GMAIL_APP_PASSWORD
        # Set up Twilio Client and SMTP connection
        self.connection = smtplib.SMTP("smtp.gmail.com")

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.email, password=self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=self.to_email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
