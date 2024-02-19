import subprocess
import cmd
import re
import os

with open('./flag.txt', 'w') as flag:
    flag.write('quarkCTF{D3lEt3D_fiL35_4r3_in-FD}')

flag = open('./flag.txt', 'r')

count = 0

'''my boss is rabbit, i've removed this for better security
def is_admin():
    print(os.popen('cat flag.txt').read())

'''

def is_safe_command(cmd):
    allow = ['cat', 'ls', 'whoami', 'cd', 'ps', 'uname', 'date', 'wc']
    ban = ['rm', 'flag.txt', 'flag', 'chall.py', 'chall']
    for i in ban:
        if i in cmd:
            return False
    for i in allow:
        if (i in cmd):
            pattern = r'^[a-zA-Z0-9/. \-]+$'
            return bool(re.match(pattern, cmd))
    return False




class CustomShell(cmd.Cmd):
    intro = "Welcome to the custom shell. Type 'exit' to quit."
    prompt = "user@rmRF$ "

    def do_exit(self, arg):
        print("Exiting...")
        return True

    def default(self, line):
        if len(line) >= 24:
            print("Command length should be less than 24 characters.")
            return

        if not is_safe_command(line):
            print("Unsafe command '{}' detected. Execution not allowed.".format(line.strip()))
            return

        try:
            global count
            if line:
                count += 1
            if count > 1 and count < 3:
                #demnnnnn cmds are runninggggggggg on my shell
                os.system('rm ./flag.txt')

            output = subprocess.check_output(line.strip(), shell=True, stderr=subprocess.STDOUT)
            print(output.decode())
        except subprocess.CalledProcessError as e:
            print("Error:", e.output.decode())
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    CustomShell().cmdloop()

