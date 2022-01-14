import logging
import argparse
import docker
from datetime import datetime
from utils import slack_utils


def create_argument_parser():
    parser = argparse.ArgumentParser(description='CHECK-APP-STATUS')
    parser.add_argument("container_name", type=str, help='Name of the container where the app is deployed')
    return parser


def get_logs_24h(container_name):
    yesterday = round(datetime.now().timestamp() - 86400)
    client = docker.from_env()
    container = client.containers.get(container_name)
    logs = container.logs(since=yesterday)
    return logs


def parse_logs(logs):
    errors = []
    criticals = []
    warnings = []
    tracebacks = []
    inside_traceback = False
    for line in logs.decode().split('\n'):
        if '[ERROR]' in line:
            errors.append(line)
        elif '[CRITICAL]' in line:
            criticals.append(line)
        elif '[WARNING]' in line:
            warnings.append(line)
        elif 'Traceback' in line:
            inside_traceback = True
            tracebacks.append(line)
        elif inside_traceback and line[0] != " ":
            tracebacks[-1] += "\n[...]\n{}\n".format(line)
            inside_traceback = False
    return errors, criticals, warnings, tracebacks


def main():
    logger = logging.getLogger(__name__)
    parser = create_argument_parser()
    args = parser.parse_args()
    logs = get_logs_24h(args.container_name)
    errors, criticals, warnings, tracebacks = parse_logs(logs)
    if any(tracebacks):
        slack_utils.report_crash(tracebacks, logger)
    else:
        slack_utils.report_daily_status(len(warnings), len(errors), len(criticals), logger)


if __name__ == "__main__":
    main()
