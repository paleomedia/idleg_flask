<?php

if (!isset($_SESSION)) { session_start(); }

require_once 'dao.php';

# Returns TRUE if PW correct

function check_login($name, $password) {
  $db = new PDO("mysql:host=127.0.0.1;port=8889;dbname=idleg_test", "root", "root");
//    $dao = new Dao();
//    $db = $dao->getConnection();
    $name = $db->quote($name);
    $rows = $db->query("SELECT password FROM users WHERE username = $name");
    if ($rows) {
        foreach ($rows as $row) {             #only one row should match  
            if ($password === $row["password"]) {
                return TRUE;
            }
        }
    }
    return FALSE;    # user not found, or wrong password
}

function ensure_logged_in() {
if (!isset($_SESSION[$name])) {
redirect("user.php", "You must login first");
}
}

function redirect($url, $flash_message = NULL) {
	if ($flash_message) {
		$_SESSION["flash"] = $flash_message;
	}
	header("Location: $url");
	die;
	}

function new_user($name, $password, $user_info) {
	$db = new PDO("mysql:host=127.0.0.1;port=8889;dbname=idleg_test", "root", "root");
	}
	?>