<?php

if (!isset($_SESSION)) { session_start(); }

# Returns TRUE if PW correct

ini_set('display_errors',1);
error_reporting(E_ALL);

/*    $host = "localhost";
    $user = "root";
    $dbpassword = "root";
    $database = "idleg_test";
    $dbport = 8889;   */

function check_login($name, $password) {
    $db = new PDO("mysql:host=127.0.0.1;port=8889;dbname=idleg_test", "root", "root");
    var_dump($db);
    $name = $db->quote($name);
    $rows = $db->query("SELECT password FROM users WHERE username = $name");
    if ($rows) {
        foreach ($rows as $row) {             #only one row should match  
            if ($password === $row["password"]) {
                return TRUE;
            }
        }
    }
    return FALSE;
}

function ensure_logged_in() {
if (!isset($_SESSION[$name])) {
redirect("user.php", "You must login first");
}
}

function redirect 
?>
