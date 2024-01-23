from crontab import CronTab
from getpass import getuser
import sys
import os
'''{os.path.abspath(os.getcwd())}/scheduled_checks_launch_script.py '''


def add_to_schedule():
    my_cron = CronTab(user=getuser())
    job = my_cron.new(command=f'python3 {os.path.abspath(os.getcwd())}/scheduled_checks/'
                              f'scripts/scheduled_checks_launch_script.py '
                              f'{sys.argv[1]}')
    job.minute.every(sys.argv[2])
    my_cron.write()
    if int(sys.argv[2]) > 1:
        minutes = 'minutes'
    else:
        minutes = 'minute'
    print(f'Auto-checking of sites in {sys.argv[1]} enabled.\n'
          f'Sites are being checked every {sys.argv[2]} {minutes}')
