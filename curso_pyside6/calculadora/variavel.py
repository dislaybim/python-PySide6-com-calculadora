#encaminha o arquivo jpg para a biblioteca, para ser executado no arquivo main

from pathlib import Path
ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'caculadora.jpg'

