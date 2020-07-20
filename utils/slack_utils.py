import os
from components import EmailIssueReference
from urllib.error import URLError, HTTPError
from slack import WebClient
from slack.errors import SlackApiError


def create_status_ok_message_block(warnings, errors, criticals):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*APP STATUS OK*   :heavy_check_mark:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "No app crashes were detected during today's scheduled log scan. Summary of today's activity:"
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
                    "text": "*Warnings detected:* {}".format(warnings)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Errors detected:* {}".format(errors)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Criticals detected:* {}".format(criticals)
                }
            ]
        },
    ]


def create_crash_alert_message_block(tracebacks):
    traceback_section = []
    for idx, traceback in enumerate(tracebacks, 1):
        traceback_section.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Traceback {}: * \n```{}```".format(idx, traceback)
                }
            }
        )

    block = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*APP CRASH DETECTED*  :x:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "The following tracebacks were found on the app's logs:"
            }
        },
        {
            "type": "divider"
        },
    ]
    block += traceback_section
    return block


def create_user_contact_form_message_block(name, email, subject, description):
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


def send_message(message_block, logger, channel='conplot'):
    try:
        slack_token = os.environ['SLACK_TOKEN']
        client = WebClient(token=slack_token)
        response = client.chat_postMessage(channel=channel, blocks=message_block)
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


def user_get_in_touch(name, email, subject, description, logger, channel='conplot'):
    msg_block = create_user_contact_form_message_block(name, email, subject, description)
    return send_message(msg_block, logger, channel)


def report_crash(tracebacks, logger, channel='conplot'):
    msg_block = create_crash_alert_message_block(tracebacks)
    return send_message(msg_block, logger, channel)


def report_daily_status(warnings, errors, criticals, logger, channel='conplot'):
    msg_block = create_status_ok_message_block(warnings, errors, criticals)
    return send_message(msg_block, logger, channel)
