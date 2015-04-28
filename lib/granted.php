<?php

session_start();

if (isset($_SESSION["access_granted"]) && !$_SESSION["access_granted"] ||
   !isset($_SESSION["access_granted"])) {
  $_SESSION["status"] = "You need to log in first";
  header("Location:index.php");
}
else {
echo "ACCESS GRANTED"; }
?>
  
<a href="logout.php">Logout</a>