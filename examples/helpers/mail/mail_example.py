import json
import os
import urllib2
from sendgrid.helpers.mail import *
from sendgrid import *

# NOTE: you will need move this file to the root directory of this project to execute properly.

def build_hello_email():
    """Minimum required to send an email"""
    from_email = Email("test@example.com")
    subject = "Hello World from the SendGrid Python Library"
    to_email = Email("test@example.com")
    content = Content("text/plain", "some text here")
    mail = Mail(from_email, subject, to_email, content)
    mail.personalizations[0].add_to(Email("test2@example.com"))

    return mail.get()

def build_kitchen_sink():
    """All settings set"""
    mail = Mail()

    mail.from_email = Email("test@example.com", "Example User")

    mail.subject = "Hello World from the SendGrid Python Library"

    personalization = Personalization()
    personalization.add_to(Email("test1@example.com", "Example User"))
    personalization.add_to(Email("test2@example.com", "Example User"))
    personalization.add_cc(Email("test3@example.com", "Example User"))
    personalization.add_cc(Email("test4@example.com", "Example User"))
    personalization.add_bcc(Email("test5@example.com"))
    personalization.add_bcc(Email("test6@example.com"))
    personalization.subject = "Hello World from the Personalized SendGrid Python Library"
    personalization.add_header(Header("X-Test", "test"))
    personalization.add_header(Header("X-Mock", "true"))
    personalization.add_substitution(Substitution("%name%", "Example User"))
    personalization.add_substitution(Substitution("%city%", "Denver"))
    personalization.add_custom_arg(CustomArg("user_id", "343"))
    personalization.add_custom_arg(CustomArg("type", "marketing"))
    personalization.send_at = 1443636843
    mail.add_personalization(personalization)

    personalization2 = Personalization()
    personalization2.add_to(Email("test1@example.com", "Example User"))
    personalization2.add_to(Email("test2@example.com", "Example User"))
    personalization2.add_cc(Email("test3@example.com", "Example User"))
    personalization2.add_cc(Email("test4@example.com", "Eric Shallock"))
    personalization2.add_bcc(Email("test5@example.com"))
    personalization2.add_bcc(Email("test6@example.com"))
    personalization2.subject = "Hello World from the Personalized SendGrid Python Library"
    personalization2.add_header(Header("X-Test", "test"))
    personalization2.add_header(Header("X-Mock", "true"))
    personalization2.add_substitution(Substitution("%name%", "Example User"))
    personalization2.add_substitution(Substitution("%city%", "Denver"))
    personalization2.add_custom_arg(CustomArg("user_id", "343"))
    personalization2.add_custom_arg(CustomArg("type", "marketing"))
    personalization2.send_at = 1443636843
    mail.add_personalization(personalization2)

    mail.add_content(Content("text/plain", "some text here"))
    mail.add_content(Content("text/html", "<html><body>some text here</body></html>"))

    attachment = Attachment()
    attachment.content = "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12"
    attachment.type = "application/pdf"
    attachment.filename = "balance_001.pdf"
    attachment.disposition = "attachment"
    attachment.content_id = "Balance Sheet"
    mail.add_attachment(attachment)

    attachment2 = Attachment()
    attachment2.content = "BwdW"
    attachment2.type = "image/png"
    attachment2.filename = "banner.png"
    attachment2.disposition = "inline"
    attachment2.content_id = "Banner"
    mail.add_attachment(attachment2)

    mail.template_id = "13b8f94f-bcae-4ec6-b752-70d6cb59f932"

    mail.add_section(Section("%section1%", "Substitution Text for Section 1"))
    mail.add_section(Section("%section2%", "Substitution Text for Section 2"))

    mail.add_header(Header("X-Test1", "test1"))
    mail.add_header(Header("X-Test3", "test2"))

    mail.add_category(Category("May"))
    mail.add_category(Category("2016"))

    mail.add_custom_arg(CustomArg("campaign", "welcome"))
    mail.add_custom_arg(CustomArg("weekday", "morning"))

    mail.send_at = 1443636842

    # This must be a valid [batch ID](https://sendgrid.com/docs/API_Reference/SMTP_API/scheduling_parameters.html) to work
    # mail.set_batch_id("N2VkYjBjYWItMGU4OC0xMWU2LWJhMzYtZjQ1Yzg5OTBkNzkxLWM5ZTUyZjNhOA")

    mail.asm = ASM(99, [4, 5, 6, 7, 8])

    mail.ip_pool_name = "24"

    mail_settings = MailSettings()
    mail_settings.bcc_settings = BCCSettings(True, Email("test@example.com"))
    mail_settings.bypass_list_management = BypassListManagement(True)
    mail_settings.footer_settings = FooterSettings(True, "Footer Text", "<html><body>Footer Text</body></html>")
    mail_settings.sandbox_mode = SandBoxMode(True)
    mail_settings.spam_check = SpamCheck(True, 1, "https://spamcatcher.sendgrid.com")
    mail.mail_settings = mail_settings

    tracking_settings = TrackingSettings()
    tracking_settings.click_tracking = ClickTracking(True, True)
    tracking_settings.open_tracking = OpenTracking(True, "Optional tag to replace with the open image in the body of the message")
    tracking_settings.subscription_tracking = SubscriptionTracking(True, "text to insert into the text/plain portion of the message", "<html><body>html to insert into the text/html portion of the message</body></html>", "Optional tag to replace with the open image in the body of the message")
    tracking_settings.ganalytics = Ganalytics(True, "some source", "some medium", "some term", "some_content", "some_campaign")
    mail.tracking_settings = tracking_settings

    mail.reply_to = Email("test@example.com")

    return mail.get()

def send_hello_email():
    # Assumes you set your environment variable:
    # https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key
    sg = SendGridAPIClient()
    data = build_hello_email()
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.headers)
    print(response.body)

def send_kitchen_sink():
    # Assumes you set your environment variable:
    # https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key
    sg = SendGridAPIClient()
    data = build_kitchen_sink()
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.headers)
    print(response.body)

send_hello_email() # this will actually send an email
send_kitchen_sink() # this will only send an email if you set SandBox Mode to False
