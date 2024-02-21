# Name: Pushpa
# Category: Stegnography 

# Author: Rohit

# Description 

> I need your help remembering a special phrase my friend used to say. I've forgotten it, but it meant a lot to us.Can you help me find it again?

# Writeup
Opened the audio file in audacity and switched to Spectrogram
We will get secret text in it which is Red Sandalwood .

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/160530927/6f650081-2824-44ea-9ae6-661f1a5a0c7c)

Red Sandalwood is password of zip file.
Extract that zip we will get image.jpg,
Now open that image in linux terminal and use exiftool command 

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/160530927/0e976628-6ea5-4b09-8c8c-c5458344f796)

Here we find some encoded text in Comment part as

xbhyrJAM{T41u-qOb7n4-U4o1-8HS4}

Now, open cryptii and decode this text with ceaser cipher method.

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/160530927/34133703-ab49-4be6-8332-d82efa923d90)


Here we get flag,

Flag:- quarkCTF{M41n-jHu7g4-N4h1-8AL4}




