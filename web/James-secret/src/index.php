<!DOCTYPE html>
<html>
<head>
    <style>
        /* Use a custom font from Google Fonts */
        @import url('https://fonts.googleapis.com/css?family=Roboto+Slab:400,700&display=swap');

        /* Use a gradient background for the body */
        body {
            font-family: 'Roboto Slab', serif;
            font-size: 16px;
            line-height: 1.5;
            color: #333;
            background: linear-gradient(to right, #446688, #57738e, #6a85a4, #7e99bd, #94aed9);
            padding: 0;
            margin: 0;
        }

        /* Add some shadow and margin to the h1 */
        h1 {
            font-size: 2rem;
            font-weight: bold;
            color: #fff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            margin: 2rem;
        }

        /* Use a grid layout for the form and make it responsive */
        form {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1rem;
        }

        /* Style the input fields and buttons */
        input[type="text"] {
            padding: 0.5rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            outline: none;
        }

        input[type="submit"] {
            padding: 0.5rem;
            border: none;
            border-radius: 4px;
            background-color: #446688;
            color: #fff;
            cursor: pointer;
            transition: transform 0.3s;
        }

        input[type="submit"]:hover {
            transform: scale(1.1);
        }

        /* Add a quark image to the top right corner of the page */
        .quark {
            position: absolute;
            top: 0;
            right: 0;
            width: 69px;
            height: 69px;
            object-fit: cover;

#output {
  /* Use a fixed width and height for the output div */
  width: 700px;
  height: 600px;
  /* Use a border and some padding to make it look nicer */
  border: 1px solid #446688;
  padding: 10px;
  /* Use a scroll bar if the content overflows */
  overflow: auto;
}


        }
    </style>
</head>
<body>

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

</body>
</html>
