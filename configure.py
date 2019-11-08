import os
import sys
import subprocess

def create_venv(venv_dirname):
    result = subprocess.run([sys.executable, '-m', 'venv', venv_dirname])
    result.check_returncode()

def install_requirements(venv_pip):
    result = subprocess.run([venv_pip, 'install', '-r', 'requirements.txt'])
    result.check_returncode()

if __name__ == '__main__':
    venv_dirname = os.getcwd() + '/' + '.venv'
    print(f"Creating python virtual environment at '{venv_dirname}'")
    create_venv(venv_dirname)
    print(f"Created python virtual environment at '{venv_dirname}'")

    print(f"Installing project dependencies")
    install_requirements(venv_dirname + "/bin/pip")
    print(f"Installed all project dependencies")
