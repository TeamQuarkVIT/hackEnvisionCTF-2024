# Merry-Go-Round
- Difficulty: Medium
- Category: Steganography and Forensics

## Author 
- [0xHarshSec](https://0xharshsec)

## Writeup
- We are provided with a favicon.png image first looking at it reveals nothing but there is a secret.txt hidden inside and can be extracted using steghide but requires a passphrase to extract it.

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/c55c1309-785d-44d5-a337-27a13b91cc35)

- The passphrase is hidden inside a robots.txt file in hckvision.teamquark.com site

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/6d1ab5a9-c96a-4ab2-af2b-1954d8aad331)

- To decode the text ```Wprz://tckxhxdc_xh_rdda``` we have to use rot

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/61af3ac4-b449-4156-a3b7-73284e7d0adb)

- We got the passphrase as ```Hack://envision_is_cool``` now we extract the secret

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/d52938ca-cc2a-4234-92f5-c2a8c61fb5a9)

- We got our secret.txt and the flag inside is ```quarkCTF{sh3rl0ck_is_h3r3}```

