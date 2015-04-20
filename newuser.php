<?php

if (!isset($_SESSION)) {
	session_start();
}

require_once("dao.php");

if (isset($_POST["username"]) && isset($_POST["password"]) && isset($_POST["email"])) {
	$username = $_POST["username"];
	$password = $_POST["password"];
	$email = $_POST["email"];

	try {
		$dao = new Dao();
		if ($dao -> newUser($username, $password, $email)) {
			$_SESSION["name"] = $username;
			$dao -> redirect("index.php", "Welcome to idleg, $username!");
		}
		else {
			$dao -> redirect("index.php", "User setup failed.");
		}
	}
	catch (Exception $e) {
		var_dump($e);
		die;
	}
}

?>