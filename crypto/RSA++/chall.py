from Crypto.Util.number import *
from secret import flag

flag = bytes_to_long(flag)

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 65537

c1 = pow(flag, e, n)
c2 = pow(flag, e, p)

print("n = ", n)
print("c1 = ", c1)
print("c2 = ", c2)
print("e = ", e)
