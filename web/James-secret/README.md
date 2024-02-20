# James-Secretan

- Difficulty: Easy
- Category: Web-Exploitation

## Writeup

- We provided no files for this challenge as it was easy and guessable. The name of the challenge gives us a hint *James Secretan* was the cover name for *James Bond*.
- We'll take a look at the Description:

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/d0946edd-e6a6-4b95-9281-978eaf072e73)

- The description says we are given access to a Secret Chat Room to try to find the secret we'll now take a look at the site

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/156e8158-d4fb-4929-9f2d-50115d476eb4)

- There is an input method; from the description, we can try the first file name, i.e. 01.txt, but if we use a direct file name it will throw us an error we need to first retrieve it from the directory so we use ```/../../../../flag/(filename)```

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/4f038043-4ad8-433d-b57b-aec7a9e85792)

- There are multiple files there but if you got the hint from the challenge name and description you just have to read the 007.txt file 007 as in James Bonds number

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/4bbdfa3d-e98a-40cf-964c-4359008a3aa2)

- We get a text as ```xbhyrJAM{I0uk_Qht3z_I0uk}``` Now to decipher it we use Caeser Cipher and shift it 7 times

![image](https://github.com/TeamQuarkVIT/hackEnvisionCTF-2024/assets/84784218/7a587fc9-5269-4bf1-89f9-05772e729453)

- BINGO! we got our flag ```quarkCTF{B0nd_Jam3s_B0nd}```
- If we take a look at index.php can see it uses the GET method to directly retrieve the files which gives us access to every files which gives rise to file inclusion vulnerability
```php
<h1>Chat Section</h1>

<!-- Add a quark image from the web search results -->
<img src="/var/www/html/favicon.png.png" alt="Quark" class="quark">

<form method="GET" action="">
    File: <input type="text" name="file" value="">
    <input type="submit" value="Submit">
</form>

<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];
    // Use the file_get_contents function to read the txt file
    $content = file_get_contents($file);
    // Use the nl2br function to preserve the line breaks
    $content = nl2br($content);
    // Use the class attribute to apply the CSS code
    echo "<p class='output'>" . $content . "</p>";
}
?>
```




  


