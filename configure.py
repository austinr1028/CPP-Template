import os
import sys
import subprocess

def create_venv(venv_dirname):
    result = subprocess.run([sys.executable, '-m', 'venv', venv_dirname])
    result.check_returncode()

def install_requirements(venv_interpreter):
    result = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'py_requirements.txt'])
    result.check_returncode()

if __name__ == '__main__':
    venv_dirname = os.getcwd() + '/' + '.venv'
    create_venv(venv_dirname)
    print(f"Created python virtual environment at '{venv_dirname}'")

    install_requirements(venv_dirname + "/bin/python")
    print(f"Installed all project dependencies")

