<?php
include('top.php');
include('users.php');

$name = $_POST["name"];
$password = $_POST["password"];

if (check_login($name, $password) {
	session_start();
	$_SESSION["name"] = $name;
	?>
	
	<p>Login successful! Welcome back, <?= $name ?>.</p>
	<?php 
}
	else {
	?>
	<p>Sorry, incorrect user name or password.</p>
	<?php
}
include('bottom.php');
?>
