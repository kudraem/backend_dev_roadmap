import requests
from datetime import datetime
import csv


class ScheduledCheckerException(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def check_accessibility(url):
    try:
        session = requests.Session()
        session.max_redirects = 5
        response = session.head(url, timeout=5.0, allow_redirects=True)
    except requests.TooManyRedirects:
        raise ScheduledCheckerException('Sorry, too many redirects')
    except requests.Timeout:
        raise ScheduledCheckerException('Timeout error. Try again later.')
    except requests.ConnectionError:
        raise ScheduledCheckerException('Connection is lost, try again later.')
    else:
        return response.status_code == 200


def get_url_list_from_file(path):
    with open(rf'{path}', 'r') as input_file:
        url_list = []
        for line in input_file:
            url_list.append(line.strip())
    return url_list


def get_url_list_from_stdin():
    url_list = []
    url = input()
    while url:
        url_list.append(url)
        url = input()
    return url_list


def check_urls(url_list):
    checks_list = []
    for url in url_list:
        try:
            url_status_200 = check_accessibility(url)
        except ScheduledCheckerException:
            url_status_200 = False
        check_time = datetime.now()
        url_check_result = [str(check_time), url, url_status_200]
        checks_list.append(url_check_result)
    return checks_list


def write_check_results_to_file(checks_result_list):
    url_status = {True: 'This site is OK', False: 'Resource is unavailable'}
    with open(r'check_result.csv', 'a') as result:
        wrighter = csv.writer(result, delimiter=';')
        for url_result in checks_result_list:
            string_template = (url_result[0:2] +
                               [url_status[url_result[2]]])
            wrighter.writerow(string_template)
        result.write('\n')


def read_check_results_from_file(path):
    test_file_result = []
    with open(rf'{path}', 'r') as result:
        reader = csv.reader(result, delimiter=';')
        for row in reader:
            if row:
                test_file_result.append(row)
    return test_file_result
