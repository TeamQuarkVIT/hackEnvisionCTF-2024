# Challenge name : avg pyjail
### category: misc
### Author : Gourav Suram

### description

> Just a simple python jail for you guys!!


# Writeup

- The challenge can be solved using `globals()` or `help()`

#### help()

```bash

└─➜ nc misc.avgjail.ctf.teamquark.com 65321         
-------- Welcome to simple python challenge ---------
Enter payload for eval : help()
Welcome to Python 3.11's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".

help>

```

- help menu in python is basically used for printing out all the functions/methods, it's argumets, etc (it's basically a man page for python).
- Here we can ask help for our challenge name, i.e it will list out all the variables, functions, and DATA inside the program.

```python
help> chall
Help on module chall:

NAME
    chall

FUNCTIONS
    challenge()

    limit_attempts(func)

    timeout_handler(signum, frame)

DATA
    attempt_limit = 5
    secret = 'quarkCTF{pyjail_fl4gs_are_FR33_p0int5_riGHT??}'
    timeout_seconds = 10

FILE
    /challenge/chall.py


```

### Flag 

`quarkCTF{pyjail_fl4gs_are_FR33_p0int5_riGHT??}`


