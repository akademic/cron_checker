cron_checker
============

checks crontab for valid syntax and sends email with error message

Internals
=========

Program copy /etc/crontab and load it with command "crontab -u nobody"
SHELL parameter subsituted with /bin/false

On wrong crontab config syntax checker sends error from crontab utility on emails hardcoded in utils.py
