<?php
// handler.php
// handle comment posts, saving to MySQL and redirecting back to the list

if (!isset($_SESSION)) {
	session_start();
}

require_once("classes/dao.php");

  if (isset($_SESSION["name"]) && isset($_POST["commentButton"])) {
    $comment = $_POST["comment"];
    $comment_type = $_POST["vote"];
    $bill = $_POST["bill"];
    $username = $_SESSION["name"];

    try {
      $dao = new Dao();
      $dao->saveComment($username, $comment, $bill, $comment_type);
    }
      catch (Exception $e) {
      var_dump($e);
      die;
    }
  }
    else {
			$dao = new Dao();
			$dao -> redirect("../index.php", "Please log in to comment.");
		}

  header("Location:../index.php");