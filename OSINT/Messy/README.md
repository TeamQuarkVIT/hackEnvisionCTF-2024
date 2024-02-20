# Messy
- Difficulty: Easy
- Category: OSINT

## Author
- [0xHarshSec](0xharshsec.me)

## Description
> Find the hidden hint and name the person who said it replace whitespaces with _ name is not case sensitive.

> Flag Format: quarkCTF{nameoftheperson}

### Writeup 
- In this challenge, we are provided with an image and a description saying the flag is the name of the person who said it, now the picture is of Messi but if we take a look at the EXIF metadata we see a comment ```The little boy from Rosario, Santa Fe, has just pitched up in heaven. He climbs into a galaxy of his own. He has his crowning moment and of course he is not alone.```

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/7b1b1199-9d92-4f29-9007-663ef876ca4e)

- Now if we do some OSINT on this dialogue we see that it was said by Peter Drury.

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/d35f4c2c-a39a-45dd-81a5-6e650b20af92)

- The Description said to use underscore instead of spaces therefore our flag is ```quarkCTF{peter_drury}```
