from os import popen

flag = "quarkCTF{sh3ll_1s_4w3s0m3}"  # will redact this ofc :P


def shell(cmd):
    if cmd == "exit":
        exit(0)
    else:
        print(popen(cmd).read())
    return popen("sha256sum data.txt").read().split()[0]


if __name__ == "__main__":
    sha_256_sum = "f2cc48f316040176046b1886df22c3d21de785eb26ed7383f6a168e2255b85ae"
    # permission of data.txt is 400 i.e only read permission.

    print("Your goal is to change the hash value of data.txt")

    while True:
        user_input = input("Enter cmd : ")
        if shell(user_input) != sha_256_sum:
            print("You did it!!")
            print(flag)
        else:
            print("Try again!!")
            continue
