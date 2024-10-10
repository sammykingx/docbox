from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
from django.conf import settings


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

    try:
        email_msg.send()

    except BadHeaderError:
        return False

    return True
