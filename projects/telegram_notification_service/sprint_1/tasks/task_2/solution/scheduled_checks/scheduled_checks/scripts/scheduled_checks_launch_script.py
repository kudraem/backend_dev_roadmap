import scheduled_checks.scheduled_checks as s_c
import sys


def enable_scheduled_checks(path):
    url_list = s_c.get_url_list_from_file(path)
    check_result = s_c.check_urls(url_list)
    s_c.write_check_results_to_file(check_result)


enable_scheduled_checks(sys.argv[1])
