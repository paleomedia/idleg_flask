<?php
$thisPage="Lawmakers"; 
include 'top.php'; ?>
  
<div class="maincontainer">
   
<?php include 'dash.php'; ?>

  <div class="billmain">
  
  <?php

    $host = "localhost";
    $user = "root";
    $dbpassword = "root";
    $database = "idleg_test";
    $dbport = 8889;

    $db = new PDO("mysql:host=$host;dbname=$database;port=$dbport", $user, $dbpassword);
    
<?php include 'footer.php'; ?>