import subprocess
import os
def run_command(command):
    try:
        result=subprocess.run(command,shell=True)
    except Exception as e:
        print("Error: ",e)
def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Directory Not Found")
def get_current_directory():
    return os.getcwd()