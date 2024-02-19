#!/usr/bin/python3

import signal
from functools import wraps

secret = 'quarkCTF{pyjail_fl4gs_are_FR33_p0int5_riGHT??}'
attempt_limit = 5
timeout_seconds = 10

def timeout_handler(signum, frame):
    print("\nTimeout reached. Exiting...")
    exit(0)

def limit_attempts(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(attempt_limit):
            func(*args, **kwargs)
        print("Exceeded attempt limit. Exiting...")
        exit(0)
    return wrapper

@limit_attempts
def challenge():
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)
    try:
        inp = input("Enter payload for eval : ")
        signal.alarm(0)
        if len(inp) < len('print(secret)') - 1 and 'secret' not in inp:
            print(eval(inp))
        else:
            print('Nice try (ig)')
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt. Exiting...")
        exit(0)

if __name__ == "__main__":
    print('-------- Welcome to simple python challenge ---------')
    challenge()
