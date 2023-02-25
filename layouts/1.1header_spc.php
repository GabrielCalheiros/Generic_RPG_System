<?php
function print_header_scp($lang, array $_TXT): array{
  /*    <link id="base" rel="stylesheet" href="./layouts/layout.css">

     */

    echo '
    <!DOCTYPE html>
    <head>

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link id="themeStylesheet" rel="stylesheet" href="./layouts/themes/Black&White.css">


    <title>'.$_TXT[0].'</title>
    <link rel="shortcut icon" type="image/jpg" href="./images/favicon.svg">


    </head>
    <body id="body" class="light-mode"><br>
    <div class="two_divisions">
    <div class="two_divisions_left">
    <form method="post">
        <button type="submit" name="lang" value="en" title="Toggle language to English">English</button>
        <button type="submit" name="lang" value="pt" title="Mudar Língua para Português">Português</button>
      </form>
    </div>
    <div class="two_divisions_right" style="text-align: end;">
    <form action="./" method="post">
    <select name="themeSelect" id="themeSelect">
        <option value="Black&White">'.$_TXT[5].'</option>
        <option value="White&Black">'.$_TXT[6].'</option>
        <option value="Black&Red">'.$_TXT[7].'</option>
        <option value="White&Green">'.$_TXT[8].'</option>
    </select>
    <input type="submit" value="'.$_TXT[9].'">

</form>
    </div>
  </div>
  <hr>

  <h1><strong>'.$_TXT[0].'</strong></h1>
  
  
 
    ';
    return $_TXT;

}



?>

