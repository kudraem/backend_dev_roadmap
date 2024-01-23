import sys
from crontab import CronTab
from scheduled_checks.scheduled_checks import write_check_results
from getpass import getuser


def enable_scheduled_checks():
    with open(rf'{sys.argv[1]}', 'r') as input_file:
        url_list = []
        for line in input_file:
            url_list.append(line.strip())

    my_cron = CronTab(user=getuser())
    job = my_cron.new(command=write_check_results(url_list))
    job.minute.every(int(sys.argv[2]))
    my_cron.write()
    if int(sys.argv[2]) > 1:
        minutes = 'minutes'
    else:
        minutes = 'minute'
    print(f'Auto-checking of sites in {sys.argv[1]} enabled.\n'
          f'Sites are being checked every {sys.argv[2]} {minutes}')
