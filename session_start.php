<?php

if (!isset($_SESSION)) {
session_start();
}

if (isset($_SESSION["flash"])) {
	?>
	<div id="flash"> <?= $_SESSION["flash"] ?> </div>
	<?php
	unset($_SESSION["flash"]);
	}

 
 
/*  if (isset($_SESSION["access_granted"]) && $_SESSION["access_granted"]) {
    header("Location:granted.php");
  }

  $user = "";
  if (isset($_SESSION["user_preset"])) {
    $user = $_SESSION["user_preset"];
  }  */
?>