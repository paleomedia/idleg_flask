<?php

session_start();
include 'users.php';

if (check_login($_POST["username"], $_POST["password"])) {
  $_SESSION["access_granted"] = true;
  header("Location:granted.php");

} else {
  $status = "Invalid username or password";
  $_SESSION["status"] = $status;
  $_SESSION["user_preset"] = $_POST["user"];
  $_SESSION["access_granted"] = false;

  header("Location:index.php");
}
?>