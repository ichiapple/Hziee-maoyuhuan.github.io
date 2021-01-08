#!C:\Users\MYH\Documents\GitHub\Hziee-maoyuhuan.github.io\learning\python\Example_code\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'zxing==0.12','console_scripts','zxing'
__requires__ = 'zxing==0.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('zxing==0.12', 'console_scripts', 'zxing')()
    )
