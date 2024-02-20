# GotEm
- Difficulty: Easy
- Category: OSINT

## Author
- [0xHarshSec](https://0xharshsec.me)

## Description
> Can you deliver justice to Gotham, a hacker villian named *V3ng3_nc3* is terrorizing the internet find him and bring him to justice along with the flag, he seems to be active on a forums and Social media.

### Writeup
- We search for person named V3ng3_nc3 on all platform and come across a profile on [Twitter](https://twitter.com/V3ng3_nc3)

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/eb72a972-dca5-42f1-a20e-802477f47962)

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/fde2d4b1-f4ff-4af5-bea2-8cbc11d4faa6)

-If we see his latest tweet he said his reddit is rekt so we try to find him on reddit, and eventually we do come across his account [Reddit](https://www.reddit.com/user/V3ng3_nc3/)

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/0126bf58-d02e-40f5-ac02-1150f22d43c9)

- He said something about nobody saw the secret means he posted something and later deleted it so we use wayback machine to see if we can find anything.

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/90d22c9c-8257-4cd5-a33f-2aaff56cbd26)

- We see a code secret reddit post we click on it and see what hides there

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/403c6dcf-66d6-4548-94b1-3709377d6f7e)

- We see a ciphered text there we try to decipher it but we can do it in two ways bruteforce rot or use the intended method caeser cipher but we need to know how many shift for this we take the help of the post it said batmans secret code debut after search for a while I found this

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/bf5c2821-15d3-48a2-945c-cabb7889b325)


- So we shift it 91939 times and we get our flag ```quarkCTF{!_am_V3ng3@nc3}```

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/2f2176ef-547b-4687-8a56-aadad884d7b9)



