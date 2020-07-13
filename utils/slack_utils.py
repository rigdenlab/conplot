import os
from components import EmailIssueReference
from urllib.error import URLError, HTTPError
from slack import WebClient
from slack.errors import SlackApiError


def create_message_block(name, email, subject, description):
    if subject == EmailIssueReference.BUG.value:
        subject = 'Bug report :beetle:'
    elif subject == EmailIssueReference.FORGOT_PSSWRD.value:
        subject = 'I forgot my password :lock:'
    elif subject == EmailIssueReference.OTHER.value:
        subject = 'Other'
    else:
        subject = 'Unkown {}'.format(subject)

    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "A new contact form has been submitted! :bell:"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Author:* {}".format(name)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Email: * {}".format(email)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Subject: * {}".format(subject)
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Message: * {}".format(description)
            }
        },
        {
            "type": "divider"
        }
    ]


def send_slack_message(name, email, subject, description, logger, channel='conplot'):
    try:
        slack_token = os.environ['SLACK_TOKEN']
        client = WebClient(token=slack_token)
        msg_block = create_message_block(name, email, subject, description)
        response = client.chat_postMessage(channel=channel, blocks=msg_block)
        logger.info("Contact form submitted: {} - {} - {}".format(name, email, subject))
    except KeyError:
        logger.error('Cannot find SLACK_TOKEN environment variable!')
        return False
    except (URLError, HTTPError) as e:
        logger.error('Impossible to establish connection! {}'.format(e))
        return False
    except SlackApiError as e:
        logger.error('Cannot send message through slack: {}'.format(e.response['error']))
        return False

    return True
