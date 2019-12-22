'''
Send the information of cancellations and supplementary classes to slack.
'''
import json
import os
import re
import time
from typing import Dict

import click
import schedule
import slackweb

from connect import ConnectWeb


def check_class(directory: str, slack_webhook: str, user_id: str, password: str) -> None:
    '''
    Scraping the element obtained from UNIPA, extract necessary information,
    add log to json and send to slack bot.

    Args:
        directory (str): Directory for saving log.json.
        slack_webhook (str): Incoming Webhook URL.
        user_id (str): Student ID number to log in to UNIPA.
        password (str): Password to log in to UNIPA.
    '''
    elements = {}

    unipa = ConnectWeb(user_id, password)
    get_log = unipa.get()
    unipa.quit()

    if get_log == '':
        return

    print('='*30)
    print(get_log)
    print('='*30)

    get_log_list = get_log.split('\n')
    for log_line in get_log_list:
        find_chanceled_class = re.search(
            r'【千住・(?P<data>.+)】(?P<text>.+)\[.+$', log_line)
        if find_chanceled_class:
            elements[find_chanceled_class.group(
                'text')] = find_chanceled_class.group('data')

    log = check_log(elements, directory)
    notice_slack(slack_webhook, log)


def check_log(elements: Dict[str, str], directory: str) -> Dict[str, str]:
    '''
    Compare the argument log with the log in the saved json file,
    return the elements that are not in the json file, and add it to the json file.

    Args:
        elements (Dict[str, str]): Log with information on canceled classes and supplementary classes.
        directory (str): Directory for saving json files.

    Returns:
        Dict[str, str]: The log which did not exist in the json file
                        by comparing the log of the json file and the argument.
    '''
    log = {}
    new_log = {}
    json_path = os.path.join(directory, 'log.json')
    if os.path.isfile(json_path):
        with open(json_path, mode='r') as json_element:
            log = json.load(json_element)
    else:
        with open(json_path, mode='w'):
            pass

    for data in elements:
        if data not in log:
            new_log[data] = elements[data]

    for data in new_log:
        log[data] = new_log[data]

    with open(json_path, mode='w') as json_element:
        json.dump(log, json_element, indent=4)

    return new_log


def notice_slack(slack_webhook: str, log: Dict[str, str]) -> None:
    '''
    Use the `Incoming Webhook` to send information about classes canceled and supplementary classes to slack

    Args:
        slack_webhook (str): URL to use `Incoming Webhook`.
        log (Dict[str, str]): Cancellation and supplementary information to be sent.
    '''
    slack = slackweb.Slack(url=slack_webhook)
    for data in log:
        print(f'Submit Slack: {data}')
        slack.notify(text=f'【{log[data]}】{data}')


@click.command()
@click.option('--directory', prompt=True, type=click.Path(exists=True), help='Directory for saving log.json.')
@click.option('--slack_webhook', prompt=True, help='Incoming Webhook URL.')
@click.option('--user_id', prompt=True, help='Student number.')
@click.option('--password', prompt=True, hide_input=True, help='Password.')
def main(directory: str, slack_webhook: str, user_id: str, password: str) -> None:
    '''
    Runs only for the specified time.

    Args:
        directory (str): Directory for saving log.json.
        slack_webhook (str): Incoming Webhook URL.
        user_id (str): Student ID number to log in to UNIPA.
        password (str): Password to log in to UNIPA.
    '''
    for hour in range(6, 22):
        if hour < 10:
            hour_time = f'0{hour}:00'
        else:
            hour_time = f'{hour}:00'
        schedule.every().day.at(hour_time).do(
            check_class, directory=directory, slack_webhook=slack_webhook, user_id=user_id, password=password)
        print(hour_time, end=' | ')
    print('\n'+'-'*30)
    print('Run start.')

    check_class(directory, slack_webhook, user_id, password)

    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()  # pylint: disable=E1120
