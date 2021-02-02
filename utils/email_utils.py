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
go to www.conplot.org/contact and complete the form. You will need to include the following verification code:

Verification Code: {}

This is an automated email, please do not reply to this message. To get in touch with us again, use to the form at 
www.conplot.org/account-recovery
    
Best wishes,
The ConPlot Team
""".format(secret)

    try:
        register_mail()
        send_email(email, subject, body)
        logger.info('Sent email to {} - {} for password recovery'.format(username, email))
        return True
    except Exception as e:
        logger.error('Cannot send recovery meail to {} - {}. Exception found: {}'.format(username, email, e))
        return False
