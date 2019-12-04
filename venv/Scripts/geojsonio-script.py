#!c:\users\syou266\cus1166_individualproject\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'geojsonio==0.0.3','console_scripts','geojsonio'
__requires__ = 'geojsonio==0.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('geojsonio==0.0.3', 'console_scripts', 'geojsonio')()
    )
