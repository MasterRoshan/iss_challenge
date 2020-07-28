#!C:\Users\TJ\Projects\isschallenge\iss\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'iss-io==0.1','console_scripts','iss_io'
__requires__ = 'iss-io==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('iss-io==0.1', 'console_scripts', 'iss_io')()
    )
