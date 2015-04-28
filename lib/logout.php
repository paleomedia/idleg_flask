<?php
session_start();

$_SESSION = array();

// session_regenerate_id(TRUE);

if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000,
        $params["path"], $params["domain"],
        $params["secure"], $params["httponly"]
    );
}

setcookie("username", "", time() - 1);

session_destroy();

header("Location:../index.php");
?>