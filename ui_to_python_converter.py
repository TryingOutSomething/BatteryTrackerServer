import subprocess
from os.path import abspath, exists


def main():
    _SOURCE_UI_TEMPLATE_FILENAME = 'interface_design.ui'
    _UI_SOURCE_FILE_PATH: str = abspath(f'./gui/design_template/{_SOURCE_UI_TEMPLATE_FILENAME}')

    if not exists(_UI_SOURCE_FILE_PATH):
        raise FileNotFoundError('UI file does not exists!')

    _DESTINATION_UI_TEMPLATE_FILENAME = 'app_template.py'
    _UI_DESTINATION_FILE_PATH: str = abspath(f'./gui/{_DESTINATION_UI_TEMPLATE_FILENAME}')
    _CONVERSION_COMMAND = ['pyside6-uic.exe', _UI_SOURCE_FILE_PATH, '-o', _UI_DESTINATION_FILE_PATH]

    output = subprocess.run(_CONVERSION_COMMAND,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            text=True)
    if not output.stdout:
        return

    print(output.stdout)


if __name__ == '__main__':
    main()
