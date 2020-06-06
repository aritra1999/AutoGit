import os

repo_name = "CP-IDE"
cmd = {
    "add":"git add .",
    "commit": "git commit -m ",
    "push": "git push https://aritra1999:abc*9051889339@github.com/aritra1999/" + repo_name + ".git master",
    "pull": "git pull https://aritra1999:abc*9051889339@github.com/aritra1999/" + repo_name + ".git master",
    "chckout": "git checkout", 
    "remote": "git remote -v",
    "status": "git status"
}

class out:
    def log(message):print("\033[92m[ LOG ] "  + message + "\033[0m ")
    def custom_input(question): return input("\033[3;37m" + question + "\033[0m")
    def error(message):print("\033[31m[ ERROR ] "  + message + "\033[0m ")

class commands: 
    def git_push():
        out.log("Push initiated.")

        # Adding changes
        out.log("Executing: " + cmd["add"])
        os.system(cmd["add"])

        # Commit chnages
        # commit = input("\n\033[37mCommit message: \033[37m")
        commit = out.custom_input("Commit message: ")
        out.log("Executing: " + cmd["commit"] + '"' + commit + '"')
        
        os.system(cmd["commit"] + '"' + commit + '"')

        # Pushing changes
        out.log("Pushing repo to master...")
        os.system(cmd["push"])

        out.log("Successful!")    

    def git_pull():
        out.log("Pull initiated.")
        out.log("Pulling repo from master...")
        os.system(cmd["pull"])


    def git_status():
        out.log(repo_name + " status.")
        os.system(cmd["status"])

if __name__ == "__main__":
    
    task_cmd = out.custom_input("Task: ")

    if task_cmd == "push":
        commands.git_push()
    elif task_cmd == "pull":
        commands.git_pull()
    elif task_cmd == "status":
        commands.git_status()
    else: 
        out.error('Invalid task!')

    print("\n")

# print("\033[0;37;40m Normal text\n")
# print("\033[2;37;40m Underlined text\033[0;37;40m \n")
# print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
# print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
# print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
# print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
# print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
# print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
# print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
# print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
# print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
# print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
# print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
# print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")
 
