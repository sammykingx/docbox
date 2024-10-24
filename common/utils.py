from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
from django.conf import settings
from common.logger import logger
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

    except (smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError):
        logger.error("could not connect to server/servr unavailable")
        return False
    
    except smtplib.SMTPRecipientsRefused as err:
        logger.error(err)
        return False
    
    except BadHeaderError:
        return False
    
    except Exception:
        logger.error(f"UNCAUGHT EXCEPTION: {err}", exc_info=True)
        return  False


    logger.info("Email Sent to User successfully ✅")
    return True
