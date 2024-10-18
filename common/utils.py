from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
from django.conf import settings
import smtplib


def deliver_email(
    mail_heading: str,
    mail_msg: str,
    recipient: list,
    reply_to: list | None = None,
) -> bool:
    """delivers email message to the receiver using the default email
    configurations of the django project
    """

    email_msg = EmailMessage(
        subject=mail_heading,
        body=mail_msg,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient,
        reply_to=reply_to,
    )
    email_msg.content_subtype = "html"
    
    try:
        email_msg.send()
        print("Email Sent to User successfully ✅")

    except (smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError):
        print("could not connect to server/servr unavailable")
        return False
    
    except smtplib.SMTPRecipientsRefused as err:
        print(err)
        return False
    
    except BadHeaderError:
        return False
    
    except Exception:
        print(f"UNCAUGHT EXCEPTION: {err}")
        return  False

    return True
