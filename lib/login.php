<?php

if (!isset($_SESSION)) {
	session_start();
}

require_once("classes/dao.php");

if (isset($_POST["username"]) && isset($_POST["password"])) {
	$name = $_POST["username"];
	$password = $_POST["password"];

	try {
		$dao = new Dao();
		if ($dao -> check_login($name, $password)) {
			$_SESSION["name"] = $name;
			
			if ($_POST['rememberme']=1) {
				$expireTime = time() + 60*60*24*180;   # 180 days from now
				setcookie("username", $_SESSION["name"], $expireTime); }
				
			$dao -> redirect("../index.php", "Login successful! Welcome back, $name.");
		}
		else {
			$dao -> redirect("../index.php", "Incorrect user name and/or password.");
		}
	}
	catch (Exception $e) {
		var_dump($e);
		die;
	}
}

?>