import os
from components import EmailIssueReference
from urllib.error import URLError, HTTPError
from slack import WebClient
from slack.errors import SlackApiError


def app_status_ok_message_block(initated_sessions, n_requests, avg_time, n_users, n_sessions, db_size):
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
                    "text": "*Number of sessions initiated:* {}".format(initated_sessions)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Number of requests served:* {}".format(n_requests)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Average request completion time:* {}".format(avg_time)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*No. of users recorded in PostgreSQL :* {}".format(n_users)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*No. of sessions recorded in PostgreSQL :* {}".format(n_sessions)
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Total PostgreSQL database size:* {}".format(db_size)
                }
            ]
        }
    ]


def app_crash_alert_message_block(date, traceback):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*APP CRASH DETECTED*  :x:"
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
                    "text": "*Date:* {}".format(date)
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Context: * \n```{}```".format(traceback)
            }
        },
        {
            "type": "divider"
        }
    ]


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
