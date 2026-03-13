from shell_utils import run_command, change_directory, get_current_directory, execute_pipeline
history=[]
while True:
    current_directory=get_current_directory()
    command=input(f"myshell:{current_directory}$")
    history.append(command)
    if "|" in command:
        cmds=command.split("|")
        cmds=[c.strip().split() for c in cmds]
        execute_pipeline(cmds)
        continue
    if command=="exit":
        print("Exiting my shell")
        break
    elif command.startswith("cd "):
        path=command.split(" ",1)[1]
        change_directory(path)
    elif command=="history":
        for i,cmd in enumerate(history):
            print(f"{i+1}: {cmd}")
    elif command.strip()=="":
        continue
    elif command == "pwd":
        print(get_current_directory())
    elif command == "ls":
        run_command("dir")
    else:
        run_command(command)
