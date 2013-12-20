#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os

from plumbum.cmd import crontab

import utils

tmpdir = os.path.dirname(os.path.realpath(__file__))+'/tmp/'

tmpfile_path = tmpdir+'crontab'

if not os.path.exists(tmpdir):
    os.makedirs(tmpdir)

def get_current_config():
    with open ('/etc/crontab', 'r') as myfile:
        data = myfile.read()
    data = data.replace('SHELL', 'SHELL=/bin/false\n#SHELL')
    return data

def check_config(data):
    with open (tmpfile_path, 'w') as tmpfile:
        tmpfile.write(data)

    p = crontab.popen(('-u', 'nobody', tmpfile_path))
    stdout, stderr = p.communicate()
    
    if stderr != '':
        return (False, stderr)
    else:
        return (True, '')

def check_crontab_exists():
    p = crontab.popen(('-u','nobody', '-l'))
    stdout, stderr = p.communicate()

    if stderr.strip() == 'no crontab for nobody':
        return False

    return True

def remove_config():
    crontab( '-u', 'nobody', '-r')

def test_syntax():
    data = get_current_config()
    test_result, message = check_config(data)

    if not test_result:
        utils.notify('Crontab config error', message, debug=True)

    crontab_exists = check_crontab_exists()

    if crontab_exists:
        remove_config()

if __name__ == '__main__':
    test_syntax()
