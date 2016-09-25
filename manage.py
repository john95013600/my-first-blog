#!/usr/bin/env python
import os
import sys
sys.path.append('C:/Users/nclab/AppData/Local/Programs/Python/Python35/Lib/site-packages')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
