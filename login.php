<?php

include('users.php');

if (isset($_POST["username"]) && isset($_POST["password"])) {
$name = $_POST["username"];
$password = $_POST["password"];

if (check_login($name, $password)) {
	$_SESSION["name"] = $name;
	redirect("index.php", "Login successful! Welcome back, $name.");
	} else {
	redirect("index.php", "Incorrect user name and/or password.");
	}
}
?>