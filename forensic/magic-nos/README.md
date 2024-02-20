# Dynamo
- The name of the challenge is Dynamo as he was a magician and this challenge is related to magic numbers, first we'll open the file in an hex editor

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/00e2609b-a77b-40c9-aec6-76f7a9c097af)

- We can see these three header number feels a bit odd so we try to look at the end header to know the file type and replace with it's appropriate header.
- The png header matches the criteria as the original header is ```89 50 4E 47 0D 0A 1A 0A``` and the latered one is ```89 69 69 69 0D 0A 1A 0A``` so we replace the 69 with appropriate number and save the file os .png extension and now we can see the flag inside the image


![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/74499c3b-8add-4f0b-8786-b09f96159098)
