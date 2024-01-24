from crontab import CronTab
from getpass import getuser
import sys
import os


def add_to_schedule():
    my_cron = CronTab(user=getuser())
    job = my_cron.new(command=f'cd {os.getcwd()}/ && '
                              f'/home/{os.getcwd()}/.local/bin/poetry run run_check url_list '
                              f'> {os.getcwd()}/cron_debug.log 2>&1')
    job.minute.every(sys.argv[2])
    my_cron.write()
    if int(sys.argv[2]) > 1:
        minutes = 'minutes'
    else:
        minutes = 'minute'
    print(f'Auto-checking of sites in {sys.argv[1]} is enabled.\n'
          f'Sites are being checked every {sys.argv[2]} {minutes}')
