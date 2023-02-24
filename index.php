<?php
session_start();//To register the chosen language, we have to start the session first 
if (!isset($_SESSION["lang"])) { $_SESSION["lang"] = "en"; }//If the language is not chosen, we will set it to English by default
if (isset($_POST["lang"])) { $_SESSION["lang"] = $_POST["lang"]; }//When the “switch language” form is submitted, we change to the selected language
require "./languages/lang-" . $_SESSION["lang"] . ".php";//Lastly, load the language file
$pageTitle = 'Layout';
require './layouts/1.header.php'; 
require './layouts/2.footer.php';
require './layouts/3.menu.php';

print_header($_TXT[0]);

$items = [
  'Rules'=>'1.0_Presentation.html',
  'References'=>'1.0_Presentation.html',
  'How to Contribute'=>'1.0_Presentation.html',
  'Downloads'=>'1.0_Presentation.html',
];

listMenu($items);


print_footer('footer');
?>




