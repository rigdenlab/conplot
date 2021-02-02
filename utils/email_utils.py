import os
import yagmail
from utils import UrlIndex


def send_email(recipient, subject, contents):
    with yagmail.SMTP(UrlIndex.CONPLOT_USERNAME.value) as yag:
        yag.send(to=recipient, subject=subject, contents=contents)


def register_mail():
    yagmail.register(UrlIndex.CONPLOT_MAIL.value, os.environ['MAIL_PSSWRD'])


def acount_recovery(username, email, secret, logger):
    subject = 'ConPlot password recovery'

    body = """
Dear ConPlot user,
    
We are sending this email because you have requested to reset your password. To regain access to your account, please
go to {} and complete the form. You will need the include the following details:

Username: {}
Email: {}
Verification Code: {}

This is an automated email, please do not reply to this message. To get in touch with us again, use to the form at 
{}
    
Best wishes,
The ConPlot Team
""".format(UrlIndex.ACCOUNT_RECOVERY.value, username, email, secret, UrlIndex.CONTACT.value)

    try:
        send_email(email, subject, body)
        logger.info('Sent email to {} - {} for password recovery'.format(username, email))
    except Exception as e:
        logger.error('Cannot send recovery meail to {} - {}. Exception found: {}'.format(username, email, e))
