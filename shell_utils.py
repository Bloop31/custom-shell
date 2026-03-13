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
def execute_pipeline(commands):
    processes = []
    prev = None

    for cmd in commands:
        if prev is None:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        else:
            p = subprocess.Popen(
                cmd,
                stdin=prev.stdout,
                stdout=subprocess.PIPE,
                shell=True
            )

        processes.append(p)
        prev = p

    output = processes[-1].communicate()[0]

    if output:
        print(output.decode(errors="ignore"))
