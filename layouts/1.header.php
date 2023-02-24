<?php
function print_header($pageTile){


    echo '
    <!DOCTYPE html>
    <head>

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="./layout.css">

    <title>'.$pageTile.'</title>
    <link rel="shortcut icon" type="image/jpg" href="./images/favicon.svg">
    <script type="text/javascript" src="./layouts/0.script.js"></script>

    </head>
    <body id="body" class="dark-mode"><br>
    <div class="two_divisions">
    <div class="two_divisions_left">
    <form method="post">
        <button type="submit" name="lang" value="en" class="lang_button_eng"></button>
        <button type="submit" name="lang" value="pt" class="lang_button_pt"></button>
      </form>
    </div>
    <div class="two_divisions_right" style="text-align: end;">
    <button type="button" name="dark_light" onclick="toggleDarkLight()" title="Toggle dark/light mode" class="theme_button"></button>
    </div>
  </div>

  <h1><strong>'.$pageTile.'</strong></h1>
  <img src="./images/cabeçalho2.svg" class="ImageCenter">
    ';
}

?>

